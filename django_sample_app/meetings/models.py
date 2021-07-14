from datetime import time

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_num = models.IntegerField()
    room_num = models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.room_num} on {self.floor_num}{self._floor_suffix(str(self.floor_num))} floor"

    def _floor_suffix(self, floor_num):
        if floor_num[-1] == "1":
            return "st"
        if floor_num[-1] == "2":
            return "nd"
        if floor_num[-1] == "3":
            return "rd"
        return "th"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"