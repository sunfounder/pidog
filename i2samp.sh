#!/bin/bash

# global variables
# =================================================================
VERSION="0.0.4"
USERNAME=${SUDO_USER:-$LOGNAME}
USER_RUN="sudo -u ${USERNAME} env XDG_RUNTIME_DIR=/run/user/$(id -u ${USERNAME})"

CONFIG="/boot/firmware/config.txt"
# Fall back to the old config.txt path
if ! test -f $CONFIG; then
    CONFIG="/boot/config.txt"
fi

ASOUND_CONF="/etc/asound.conf"

# ----- robot hat without onboard mic -----
DTOVERLAY_WITHOUT_MIC="hifiberry-dac"
AUDIO_CARD_NAME_WITHOUT_MIC="sndrpihifiberry"
ALSA_CARD_NAME_WITHOUT_MIC="snd_rpi_hifiberry_dac"

# ----- robot hat with onboard mic -----
DTOVERLAY_WITH_MIC="googlevoicehat-soundcard"
AUDIO_CARD_NAME_WITH_MIC="sndrpigooglevoi"
ALSA_CARD_NAME_WITH_MIC="snd_rpi_googlevoicehat_soundcar"

SOFTVOL_SPEAKER_NAME="robot-hat speaker"
SOFTVOL_MIC_NAME="robot-hat mic"

# ----- robot hat 5 -----
HAT_DEVICE_TREE="/proc/decvice-tree/"
HAT_UUIDs=(
    "9daeea78-0000-076e-0032-582369ac3e02",
)
ROBOTHAT5_PRODUCT_VER=50
robothat_product=""
robothat_product_id=0
robothat_product_ver=0
robothat_uuid=""
robothat_vendor=""

# ---------------------------
robothat_spk_en=20 # robothat4 GPIO20, robothat5 GPIO12
_is_install_deps=true
_is_with_mic=true
dtoverlay_name=""
audio_card_name=""
alsa_card_name=""

# function define
# =================================================================
# black     0
# red       1
# green     2
# yellow    3
# blue      4
# magenta   5
# cyan      6
# white     7
success() {
    echo -e "$(tput setaf 2)$1$(tput sgr0)"
}

info() {
    echo -e "$(tput setaf 6)$1$(tput sgr0)"
}

warning() {
    echo -e "$(tput setaf 3)$1$(tput sgr0)"
}

error() {
    echo -e "$(tput setaf 1)$1$(tput sgr0)"
}

newline() {
    echo ""
}

confirm() {
    if [ "$FORCE" == '-y' ]; then
        true
    else
        read -r -p "$1 [y/N] " response </dev/tty
        if [[ $response =~ ^(yes|y|Y)$ ]]; then
            true
        else
            false
        fi
    fi
}

sudocheck() {
    if [ $(id -u) -ne 0 ]; then
        warning "Install must be run as root. Try 'sudo bash ./i2samp.sh'"
        exit 1
    fi
}

ask_reboot() {
    read -e -p "$(tput setaf 5)$1 (Y/N): $(tput sgr0)" choice
    if [ "$choice" == "Y" ] || [ "$choice" == "y" ]; then
        info "Rebooting now ..."
        sudo sync && sudo reboot
    fi
}

get_soundcard_index() {
    card_name=$1
    if [[ -z "${card_name}" ]]; then
        error "card_name is null"
        return
    fi
    card_index=$(sudo aplay -l | grep $card_name | awk '{print $2}' | tr -d ':')
    echo $card_index
}

config_asound_without_mic() {
    # backup file
    if [ -e "${ASOUND_CONF}" ]; then
        if [ -e "${ASOUND_CONF}.old" ]; then
            sudo rm -f "${ASOUND_CONF}.old"
        fi
        sudo cp "${ASOUND_CONF}" "${ASOUND_CONF}.old"
    fi

    cat >"${ASOUND_CONF}" <<EOF

pcm.speaker {
    type hw
    card ${AUDIO_CARD_NAME_WITHOUT_MIC}
}

pcm.dmixer {
    type dmix
    ipc_key 1024
    ipc_perm 0666
    slave {
        pcm "speaker"
        period_time 0
        period_size 1024
        buffer_size 8192
        rate 44100
        channels 2
    }
}

ctl.dmixer {
    type hw
    card ${AUDIO_CARD_NAME_WITHOUT_MIC}
}

pcm.softvol {
    type softvol
    slave.pcm "dmixer"
    control {
        name "${SOFTVOL_SPEAKER_NAME} Playback Volume"
        card ${AUDIO_CARD_NAME_WITHOUT_MIC}
    }
    min_dB -51.0
    max_dB 0.0
}

pcm.robothat {
    type plug
    slave.pcm "softvol"
}

ctl.robothat {
    type hw
    card ${AUDIO_CARD_NAME_WITHOUT_MIC}
}

pcm.!default robothat
ctl.!default robothat

EOF
}

config_asound_with_mic() {
    # backup file
    if [ -e "${ASOUND_CONF}" ]; then
        if [ -e "${ASOUND_CONF}.old" ]; then
            sudo rm -f "${ASOUND_CONF}.old"
        fi
        sudo cp "${ASOUND_CONF}" "${ASOUND_CONF}.old"
    fi

    if [ $robothat_product_ver -ge ${ROBOTHAT5_PRODUCT_VER} ]; then

        #
        sudo cat >"${ASOUND_CONF}" <<EOF

pcm.robothat {
    type asym
    playback.pcm {
        type plug
        slave.pcm "speaker"
    }
    capture.pcm {
        type plug
        slave.pcm "mic"
    }
}

pcm.speaker_hw {
    type hw
    card ${AUDIO_CARD_NAME_WITH_MIC}
    device 0
}

pcm.dmixer {
    type dmix
    ipc_key 1024
    ipc_perm 0666
    slave {
        pcm "speaker_hw"
        period_time 0
        period_size 1024
        buffer_size 8192
        rate 44100
        channels 2
    }
}

ctl.dmixer {
    type hw
    card ${AUDIO_CARD_NAME_WITH_MIC}
}

pcm.speaker {
    type softvol
    slave {
        pcm "dmixer"
    }
    control {
        name "${SOFTVOL_SPEAKER_NAME} Playback Volume"
        card ${AUDIO_CARD_NAME_WITH_MIC}
    }
    min_dB -51.0
    max_dB 0.0
}

pcm.mic_hw {
    type hw
    card ${AUDIO_CARD_NAME_WITH_MIC}
    device 0
}

pcm.mic {
    type softvol
    slave {
        pcm "mic_hw"
    }
    control {
        name "${SOFTVOL_MIC_NAME} Capture Volume"
        card ${AUDIO_CARD_NAME_WITH_MIC}
    }
    min_dB -26.0
    max_dB 25.0
}

ctl.robothat {
    type hw
    card ${AUDIO_CARD_NAME_WITH_MIC}
}

pcm.!default robothat
ctl.!default robothat

EOF

    else
        sudo cat >"${ASOUND_CONF}" <<EOF

pcm.robothat {
    type asym
    playback.pcm {
        type plug
        slave.pcm "speaker"
    }
}

pcm.speaker_hw {
    type hw
    card ${AUDIO_CARD_NAME_WITH_MIC}
    device 0
}

pcm.speaker {
    type softvol
    slave {
        pcm "speaker_hw"
    }
    control {
        name "${SOFTVOL_SPEAKER_NAME} Playback Volume"
        card ${AUDIO_CARD_NAME_WITH_MIC}
    }
    min_dB -51.0
    max_dB 0.0
}

ctl.robothat {
    type hw
    card ${AUDIO_CARD_NAME_WITH_MIC}
}

pcm.!default robothat
ctl.!default robothat

EOF
    fi

}

get_sink_index() {
    card_name=$1
    if [[ -z "${card_name}" ]]; then
        error "card name is null"
        return
    fi
    index=$($USER_RUN \
        pactl -f json list sinks | jq -r \
        '.[] | select(.["properties"]["alsa.card_name"] == "'${card_name}'"
        and .["properties"]["device.class"] == "sound"
        ).index')
    echo $index
}

get_source_index() {
    card_name=$1
    if [[ -z "${card_name}" ]]; then
        error "card name is null"
        return
    fi
    index=$($USER_RUN \
        pactl -f json list sources | jq -r \
        '.[] | select(.["properties"]["alsa.card_name"] == "'${card_name}'"
        and .["properties"]["device.class"] == "sound"
        ).index')
    echo $index
}

set_default_sink() {
    sink_index=$1
    if [[ -z "${sink_index}" ]]; then
        error "sink index is null"
        return
    fi
    $USER_RUN \
        pactl set-default-sink ${sink_index}
}

set_default_source() {
    source_index=$1
    if [[ -z "${source_index}" ]]; then
        error "source index is null"
        return
    fi
    $USER_RUN \
        pactl set-default-source ${source_index}
}

set_default_sink_volume() {
    volume=$1
    if [[ -z "${volume}" ]]; then
        error "volume is null"
        return
    fi
    $USER_RUN \
        pactl set-sink-volume @DEFAULT_SINK@ ${volume}%
}

set_default_source_volume() {
    volume=$1
    if [[ -z "${volume}" ]]; then
        error "volume is null"
        return
    fi
    $USER_RUN \
        pactl set-source-volume @DEFAULT_SOURCE@ ${volume}%
}

check_robothat() {
    # find robothat device-tree directory
    hat_dirs=$(find /proc/device-tree/*hat* -type d)
    # echo $hat_dirs
    hat_dir=""

    for dir in $hat_dirs; do
        if [ ! -e "$dir"/uuid ]; then
            continue
        fi
        uuid=$(tr -d '\0' <"$dir"/uuid)
        # echo uuid:$uuid

        # ----- whether uuid in HAT_UUIDs -----
        # echo HAT_UUIDs:${HAT_UUIDs[@]}
        if [[ -n "${uuid}" && "${HAT_UUIDs[@]}" =~ "${uuid}" ]]; then
            hat_dir=$dir
            break
        fi
    done

    echo hat_dir:$hat_dir
    if [[ -z "${hat_dir}" ]]; then
        echo "No robothat 5 found"
        return
    fi

    # read robothat info
    robothat_product=$(tr -d '\0' <"$hat_dir"/product)
    robothat_product_id_hex=$(tr -d '\0' <"$hat_dir"/product_id)
    robothat_product_ver_hex=$(tr -d '\0' <"$hat_dir"/product_ver)
    let robothat_product_id=$(printf "%d" $robothat_product_id_hex)
    let robothat_product_ver=$(printf "%d" $robothat_product_ver_hex)

    robothat_uuid=$(tr -d '\0' <"$hat_dir"/uuid)
    robothat_vendor=$(tr -d '\0' <"$hat_dir"/vendor)

    success "Found:"
    success "  Product: $robothat_product"
    success "  Product ID: $robothat_product_id ($robothat_product_id_hex)"
    success "  Version: $robothat_product_ver ($robothat_product_ver_hex)"
    success "  Vendor: $robothat_vendor"
    success "  UUID: $robothat_uuid"
}

# main_fuction
# ================================================================================
install_soundcard_driver() {
    info "install robot-hat soundcard driver >>>"
    info "script version: $VERSION"
    info "user: $USERNAME"

    # check root
    # =====================================
    sudocheck

    # apt install packages
    # =====================================
    if $_is_install_deps; then
        newline
        info "apt update..."
        apt update

        info "install alsa-utils ..."
        # alsa-utils includes:
        #  alsamixer, aplay, arecord, amixer, speaker-test
        apt install alsa-utils -y

        info "install pulseaudio ..."
        apt install pulseaudio -y

        info "install pulseaudio-utils ..."
        apt install pulseaudio-utils -y

        info "install jq ..."
        apt install jq -y

        info "install sox ..."
        apt install sox -y
    else
        info "skip install deps ..."
    fi

    # detect robothat 5
    # =====================================
    newline
    info "check robothat 5 ..."
    check_robothat

    if [ $robothat_product_ver -ge ${ROBOTHAT5_PRODUCT_VER} ]; then
        robothat_spk_en=12
        _is_with_mic=true
    else
        robothat_spk_en=20
        _is_with_mic=false
    fi
    success "robothat_spk_en: ${robothat_spk_en}"
    success "is_with_mic: ${_is_with_mic}"

    # config soundcard
    # =====================================
    newline
    if $_is_with_mic; then
        info "config soundcard with mic ..."
        dtoverlay_name=${DTOVERLAY_WITH_MIC}
        audio_card_name=${AUDIO_CARD_NAME_WITH_MIC}
        alsa_card_name=${ALSA_CARD_NAME_WITH_MIC}
    else
        info "config soundcard without mic ..."
        dtoverlay_name=${DTOVERLAY_WITHOUT_MIC}
        audio_card_name=${AUDIO_CARD_NAME_WITHOUT_MIC}
        alsa_card_name=${ALSA_CARD_NAME_WITHOUT_MIC}
    fi

    # --- add dtoverlay to config.txt ---
    newline
    if $_is_with_mic; then
        info "add dtoverlay ${DTOVERLAY_WITH_MIC} in ${CONFIG} ..."
        if [ -e "${CONFIG}" ]; then
            # dtoverlay=googlevoicehat-soundcard
            # #dtoverlay=hifiberry-dac
            if grep -q -e ".*dtoverlay=${DTOVERLAY_WITH_MIC}.*" "${CONFIG}"; then
                echo "activated dtoverlay ${DTOVERLAY_WITH_MIC} ..."
                sudo sed -i -e "s:.*dtoverlay=${DTOVERLAY_WITH_MIC}.*:dtoverlay=${DTOVERLAY_WITH_MIC}:g" "${CONFIG}"
                sudo sed -i -e "s:.*dtoverlay=${DTOVERLAY_WITHOUT_MIC}.*:#dtoverlay=${DTOVERLAY_WITHOUT_MIC}:g" "${CONFIG}"
            else
                echo "add dtoverlay ${DTOVERLAY_WITH_MIC} ..."
                echo "dtoverlay=${DTOVERLAY_WITH_MIC}" | sudo tee -a $CONFIG
                sudo sed -i -e "s:.*dtoverlay=${DTOVERLAY_WITHOUT_MIC}.*:#dtoverlay=${DTOVERLAY_WITHOUT_MIC}:g" "${CONFIG}"
            fi
        else
            error "${CONFIG} not found"
        fi
    else
        info "add dtoverlay ${DTOVERLAY_WITHOUT_MIC} in ${CONFIG} ..."
        if [ -e "${CONFIG}" ]; then
            # dtoverlay=googlevoicehat-soundcard
            # #dtoverlay=hifiberry-dac
            if grep -q -e ".*dtoverlay=${DTOVERLAY_WITHOUT_MIC}.*" "${CONFIG}"; then
                echo "activated dtoverlay ${DTOVERLAY_WITHOUT_MIC} ..."
                sudo sed -i -e "s:.*dtoverlay=${DTOVERLAY_WITHOUT_MIC}.*:dtoverlay=${DTOVERLAY_WITHOUT_MIC}:g" "${CONFIG}"
                sudo sed -i -e "s:.*dtoverlay=${DTOVERLAY_WITH_MIC}.*:#dtoverlay=${DTOVERLAY_WITH_MIC}:g" "${CONFIG}"
            else
                echo "add dtoverlay ${DTOVERLAY_WITHOUT_MIC} ..."
                echo "dtoverlay=${DTOVERLAY_WITHOUT_MIC}" | sudo tee -a $CONFIG
                sudo sed -i -e "s:.*dtoverlay=${DTOVERLAY_WITH_MIC}.*:#dtoverlay=${DTOVERLAY_WITH_MIC}:g" "${CONFIG}"
            fi
        else
            error "${CONFIG} not found"
        fi
    fi

    # --- load dtoverlay ---
    newline
    info "Trying to load dtoverlay ${dtoverlay_name} ..."
    dtoverlay ${dtoverlay_name}
    sleep 1

    # --- get sound card ---
    info "get_soundcard_index ..."
    card_index=$(get_soundcard_index $audio_card_name)
    if [[ -z "${card_index}" ]]; then
        error "soundcard index not found. Sometimes you need to reboot to activate the soundcard."
        ask_reboot "Would you like to reboot and retry now?"
        warning "Unfinished"
        exit 1
    else
        success "soundcard ${audio_card_name} index: ${card_index}"
    fi

    # --- config /etc/asound.conf ---
    newline
    if $_is_with_mic; then
        info "config /etc/asound.conf with mic ..."
        # write asound.conf
        config_asound_with_mic
    else
        info "config /etc/asound.conf without mic ..."
        # write asound.conf
        config_asound_without_mic
    fi
    # restart alsa-utils
    sudo systemctl restart alsa-utils 2>/dev/null
    # set volume 100%
    info "set ALSA speker volume to 100% ..."
    play -n trim 0.0 0.5 2>/dev/null # play a short sound to to activate alsamixer speaker vol control
    amixer -c ${audio_card_name} sset "${SOFTVOL_SPEAKER_NAME}" 100%
    if $_is_with_mic; then
        info "set ALSA mic volume to 100% ..."
        rec /tmp/rec_test.wav trim 0 0.5 2>/dev/null # record a short sound to activate alsamixer mic vol control
        amixer -c ${audio_card_name} sset "${SOFTVOL_MIC_NAME}" 100%
    fi

    # --- config pulseaudio ---
    newline
    info "config pulseaudio ..."

    # enable pulseaudio
    # https://www.raspberrypi.com/documentation/computers/configuration.html#audio-config-2
    info "raspi-config enable pulseaudio ..."
    raspi-config nonint do_audioconf 1 2>/dev/null

    # run pulseaudio
    info "run pulseaudio ..."
    # # stop pulseaudio
    # $USER_RUN \
    #     pulseaudio -k 2>/dev/null
    # start pulseaudio
    $USER_RUN \
        pulseaudio -D 2>/dev/null

    # get sink index
    newline
    info "get_sink_index ..."
    sink_index=$(get_sink_index $alsa_card_name)
    if [[ -z "${sink_index}" ]]; then
        error "sink index not found."
        error "Sometimes you need to reboot to activate the soundcard."
    else
        success "sink index: ${sink_index}"
    fi

    # set default sink
    info "set default sink ..."
    set_default_sink "${sink_index}"

    if $_is_with_mic; then
        # get source index
        info "get_source_index ..."
        source_index=$(get_source_index $alsa_card_name)
        if [[ -z "${source_index}" ]]; then
            error "source index not found."
            error "Sometimes you need to reboot to activate the soundcard."
        else
            success "source index: ${source_index}"
        fi
        # set default source
        info "set default source ..."
        set_default_source "${source_index}"
    fi

    # set default volume
    info "set default Pulseaudio volume to 100% ..."
    set_default_sink_volume 100
    if $_is_with_mic; then
        set_default_source_volume 100
    fi

    # --- test speaker ---
    newline
    if confirm "Do you wish to test speaker now?"; then
        info "testing speaker ..."
        # enable speaker
        if command -v pinctrl >/dev/null; then
            pinctrl set $robothat_spk_en op dh
            # play a short sound to fill data and avoid the speaker overheating
            play -n trim 0.0 0.5 2>/dev/null
        elif command -v raspi-gpio >/dev/null; then
            raspi-gpio set $robothat_spk_en op dh
            # play a short sound to fill data and avoid the speaker overheating
            play -n trim 0.0 0.5 2>/dev/null
        else
            warning "Could not find pinctrl or raspi-gpio command."
        fi
        # test speaker
        speaker-test -l3 -c2 -t wav
    fi

    # --- Done ---
    newline
    success "All done!"
    newline
}

# main
# =================================================================
for arg in "$@"; do
    case $arg in
    --no-deps)
        _is_install_deps=false
        ;;
    esac
done

# echo sink_index=$(get_sink_index)
# echo source_index=$(get_source_index)

install_soundcard_driver

exit 0
