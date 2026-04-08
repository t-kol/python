class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL
    
    def power(self):
        self.status = not self.status

    def mute(self):
        if self.status:
            if not self.muted:
                self.prev_volume = self.volume
                self.volume = 0
                self.muted = True
            else:
                self.volume = self.prev_volume
                self.muted = False

    def channel_up(self):
        if self.status == True:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        if self.status == True:
            if self.volume == 0:
                self.volume = 1
            else:
                if self.channel == Television.MIN_CHANNEL:
                    self.channel = Television.MAX_CHANNEL
                else:
                    self.channel -= 1

    def volume_up(self):
        if self.status:
            if self.muted:
                self.volume = self.prev_volume
                self.muted = False

            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        if self.status:
            if self.muted:
                self.volume = self.prev_volume
                self.muted = False

            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        return(f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}")