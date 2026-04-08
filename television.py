class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = Television.MIN_VOLUME
        self.channel: int = Television.MIN_CHANNEL
    
    def power(self) -> None:
        """
        Turns tv on and off by flipping boolean.
        """
        self.status = not self.status

    def mute(self) -> None:
        """
        If tv is on then either unmutes or mutes tv.
        If tv is muted and then is unmuted it will return to its previous volume (prev_volume).
        """
        if self.status:
            if not self.muted:
                self.prev_volume = self.volume
                self.volume = 0
                self.muted = True
            else:
                self.volume = self.prev_volume
                self.muted = False

    def channel_up(self) -> None:
        """
        If tv is on then increase channel by one.

        If channel is at the max channel then it circles around to the min channel.
        """
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self) -> None:
        """
        If tv is on then decrease channel by one.

        If channel is at the min channel then it circles around to the max channel.
        """
        if self.status:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self) -> None:
        """
        If tv is on and not muted then it increases the volume by one.

        If it is muted it reverts to the previous volume and increase by one.

        It does not increase if it is at max volume.
        """
        if self.status:
            if self.muted:
                self.volume = self.prev_volume
                self.muted = False

            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self) -> None:
        """
        If tv is on and not muted then it decreases the volume by one.

        If it is muted it reverts to the previous volume and decreases by one.

        It does not decreases if it is at min volume.
        """
        if self.status:
            if self.muted:
                self.volume = self.prev_volume
                self.muted = False

            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self) -> str:
        """
        Returns a string that includes the power status, channel number, and volume.
        """
        return(f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}")