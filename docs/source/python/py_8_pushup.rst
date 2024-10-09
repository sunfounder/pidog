.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

8. Flessioni
===============

PiDog è un robot amante dell’esercizio fisico che farà le flessioni insieme a te.

.. image:: img/py_8.gif

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 8_pushup.py

Dopo l’avvio del programma, PiDog si metterà in posizione di plank, poi eseguirà ciclicamente delle flessioni accompagnate da abbaii.


**Codice**

.. note::
    Puoi **Modificare/Resettare/Copiare/Eseguire/Interrompere** il codice riportato qui sotto. Ma prima, devi accedere al percorso del codice sorgente come ``pidog\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l’effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import push_up, bark

    my_dog = Pidog()

    sleep(0.5)

    def main():
        my_dog.legs_move([[45, -25, -45, 25, 80, 70, -80, -70]], speed=50)
        my_dog.head_move([[0, 0, -20]], speed=90)
        my_dog.wait_all_done()
        sleep(0.5)
        bark(my_dog, [0, 0, -20])
        sleep(0.1)
        bark(my_dog, [0, 0, -20])

        sleep(1)
        my_dog.rgb_strip.set_mode("speak", color="blue", bps=2)
        while True:
            push_up(my_dog, speed=92)
            bark(my_dog, [0, 0, -40])
            sleep(0.4)


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()