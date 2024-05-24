
``` mermaid
classDiagram
    class BingoSpel {
        - ALTextToSpeechProxy speech_proxy
        - ALAutonomousLifeProxy autonomous_life_proxy
        - ALVideoDeviceProxy video_service
        - string ip
        - int port
        - string language
        - int speed
        - list[list[int]] bingo_bord
        - list[int] opgeroepen_nummers
        + __init__(ip="nao.local", port=9559)
        + start_spel()
        + roep_nummer_op() int
        + speel_bingo()
        + controleer_winst() bool
        + start_qr_detection()
        + parse_qr_data(data: str)
    }

    class ALTextToSpeechProxy {
        + setLanguage(language: str)
        + setParameter(name: str, value: int)
        + say(text: str)
    }

    class ALAutonomousLifeProxy {
        + setState(state: str)
    }

    class ALVideoDeviceProxy {
        + subscribeCamera(name: str, cameraIndex: int, resolution: int, colorSpace: int, fps: int) str
        + getImageRemote(name: str) tuple
        + unsubscribe(name: str)
    }

    BingoSpel --> ALTextToSpeechProxy : Uses
    BingoSpel --> ALAutonomousLifeProxy : Uses
    BingoSpel --> ALVideoDeviceProxy : Uses
```