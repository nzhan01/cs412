from django.db import models

# Create your models here.

class Voter(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    street_number =models.IntegerField() #Residential Address -
    street_name = models.TextField() #Residential Address -
    apartment_number =models.TextField() #Residential Address -
    zip_code =models.IntegerField() #Residential Address -
    date_of_birth =models.DateField()
    date_of_registration =models.DateField()
    party_affiliation  =models.CharField(max_length=2) #(**note, this is a 2-character wide field**)
    precinct_number =models.IntegerField()

    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()

    voter_score = models.IntegerField() #A score assigned to each voter based on how many elections they voted in.

    def __str__(self):
        '''Return a string representation of this Voter model instance.'''
        return f'{self.Last_Name}, {self.First_Name} - {self.party_affiliation} - DOB: {self.date_of_birth} -Voter Score: {self.voter_score}'
    



def load_data():
    '''Function to load data records from CSV file into Django model instances.'''
    
    #Voter.objects.all().delete()

    filename = '/Users/nicholas/Dropbox/My Mac (Nicholas’s MacBook Air)/Desktop/django/newton_voters.csv'
    f = open(filename)
    f.readline() # discard headers
 
    #for row in range(5):
    for line in f:
        
        fields = line.split(',')
		

        try:
            result = Voter(
                last_name = fields[1],
                first_name = fields[2],
                street_number = int(fields[3]),
                street_name = fields[4],
                apartment_number = fields[5],
                zip_code = int(fields[6]),
                date_of_birth = fields[7],
                date_of_registration = fields[8],
                party_affiliation  = fields[9],
                precinct_number = int(fields[10]),
                v20state = fields[11]=='TRUE',
                v21town = fields[12]=='TRUE',
                v21primary = fields[13]=='TRUE',
                v22general = fields[14]=='TRUE',
                v23town = fields[15]=='TRUE',
                voter_score = int(fields[16]), 
            )
            result.save()

        except:
            print(f'Error processing line: {line}')
    
    print(f'Done. Created {len(Voter.objects.all())} Results.')