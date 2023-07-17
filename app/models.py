from django.db import models

# Create your models here.
class States(models.Model):
    Name = models.CharField(max_length=200, unique=True, verbose_name='State Name')
    Is_Union_Territory = models.BooleanField(default=False, verbose_name='Is Union Territory')

    class Meta:
        ordering = ['Is_Union_Territory', 'Name',]
        verbose_name_plural = 'States'
        indexes = [
            models.Index(fields=['Name', 'Is_Union_Territory'], name='state_index'),
        ]

    def save(self, *args, **kwargs):
        self.full_clean() # calls self.clean() as well cleans other fields
        return super(States, self).save(*args, **kwargs)

    def __str__(self):
        return self.Name


class Districts(models.Model):
    Name = models.CharField(max_length=200, verbose_name='District Name')
    state = models.ForeignKey(States, on_delete=models.CASCADE, verbose_name='State', related_name='state_districts', related_query_name='state_district')

    class Meta:
        ordering = ['state', 'Name',]
        unique_together = [['Name', 'state']]
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        indexes = [
            models.Index(fields=['Name', 'state'], name='district_index'),
        ]

    def save(self, *args, **kwargs):
        self.full_clean() # calls self.clean() as well cleans other fields
        return super(Districts, self).save(*args, **kwargs)

    def __str__(self):
        ret = str(self.state)+" - "+str(self.Name)
        return ret