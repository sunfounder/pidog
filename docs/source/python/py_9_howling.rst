.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

9. Ululato
===============

PiDog non è solo un cucciolo adorabile, ma anche un cane possente. Vieni a sentirlo ululare!

.. image:: img/py_9.gif

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 9_howling.py

Dopo l’avvio del programma, PiDog si siederà a terra e inizierà a ululare.


**Codice**

.. note::
    Puoi **Modificare/Resettare/Copiare/Eseguire/Interrompere** il codice riportato qui sotto. Ma prima, devi accedere al percorso del codice sorgente come ``pidog\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l’effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import howling

    my_dog = Pidog()

    sleep(0.5)


    def main():
        my_dog.do_action('sit', speed=50)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-40, immediately=True, speed=80)
        sleep(0.5)
        while True:
            howling(my_dog)


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()

