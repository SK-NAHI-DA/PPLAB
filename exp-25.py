class Time:
    def __init__(self,seconds):
        self.seconds=seconds
    def convert_to_minutes(self):
        mins=self.seconds//60
        secs=self.seconds%60
        return "%d:%d"%(mins,secs)
    def convert_to_hours(self):
        secs=self.seconds
        hours=secs//3600
        secs=secs%3600
        mins=secs//60
        secs=secs%60
        return "%d:%d:%d"%(hours,mins,secs)
def main():
    t1=Time(230)
    print(t1.convert_to_minutes())
    t2=Time(4520)
    print(t2.convert_to_hours())

main()
