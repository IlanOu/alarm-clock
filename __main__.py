from src.base.Waker import Waker, Alarm
from src.actions.MusicPlayers import MusicPlayer
import sys, time, signal

# if __name__ == "__main__":
#     waker = Waker()
#     waker.start()



def main():
    alarm = Alarm()
    
    # Add wake-up actions
    alarm.waker.add_action(print, ("Good morning!",))
    alarm.waker.add_action(print, ("It's time to start your day!",))
    alarm.waker.add_action(MusicPlayer.play, ["https://youtube.com/qdognqpsflsqi"])
    
    alarm.run()

    # Keep the script running
    try:
        while alarm.running:
            time.sleep(1)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    except KeyboardInterrupt:
        alarm.stop()  # You'll need to implement this method in the Alarm class
        print("Alarm clock stopped.")




if __name__ == "__main__":
    main()