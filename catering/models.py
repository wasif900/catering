from django.db import models
from .validators import file_size

# Create your models here.

class Service(models.Model):
    ser_prov_id = models.AutoField
    ser_prov_name = models.CharField(max_length=30)
    ser_prov_username = models.CharField(max_length=30)
    ser_prov_email_address = models.EmailField(max_length=70)
    ser_prov_phone_number=models.CharField(max_length=30)
    ser_prov_password = models.CharField(max_length=100)
    ser_prov_service_country = models.CharField(max_length=30)
    ser_prov_service_city = models.CharField(max_length=30)
    ser_prov_service_area = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.ser_prov_name
    

class  gigs(models.Model):
    gig_id = models.AutoField
    gig_title = models.CharField(max_length=30 ,default="")
    gig_category = models.CharField(max_length=30 ,default="")
    gig_sub_category = models.EmailField(max_length=30 ,default="")
    gig_search_tags=models.CharField(max_length=60 ,default="")
    gig_package_detail_basic_name= models.CharField(max_length=30,default="")
    gig_package_detail_standard_name= models.CharField(max_length=30,default="")
    gig_package_detail_premium_name= models.CharField(max_length=30,default="")
    gig_package_detail_basic_detail= models.CharField(max_length=100,default="")
    gig_package_detail_standard_detail= models.CharField(max_length=100,default="")
    gig_package_detail_premium_detail= models.CharField(max_length=100,default="")
    gig_package_detail_basic_delivery_time= models.CharField(max_length=3,default="")
    gig_package_detail_standard_delivery_time= models.CharField(max_length=30,default="")
    gig_package_detail_premium_delivery_time= models.CharField(max_length=30,default="")
    gig_package_detail_basic_price= models.CharField(max_length=30,default="")
    gig_package_detail_standard_price= models.CharField(max_length=30,default="")
    gig_package_detail_premium_price= models.CharField(max_length=30,default="")
    gig_package_details= models.CharField(max_length=300,default="" )
    gig_city = models.CharField(max_length=50,default="" )
    gig_country = models.CharField(max_length=100,default="" )
    # gig_package_detail_standard_detail_brief= models.CharField(max_length=300)
    # gig_package_detail_premium_detail_brief= models.CharField(max_length=300)
    
    gig1_image=models.ImageField(upload_to="user_images" ,default="")
    gig2_image=models.ImageField(upload_to="user_images"  ,default="")
    gig3_image=models.ImageField(upload_to="user_images"  ,default="")
    gig_vedio = models.FileField(upload_to="usr_video/%y",validators=[file_size] ,default="")
    gig_user= models.CharField(max_length=30,default="")

    

    def __str__(self) -> str:
        return self.gig_title
    
# class  gigs_gallery(models.Model):

#       def __str__(self) -> str:
#         return self.gig_title
