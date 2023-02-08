from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    excel_file = models.FileField(upload_to='excel/')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.date_of_birth) + ' ' + str(self.excel_file)
