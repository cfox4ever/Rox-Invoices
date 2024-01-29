from django.db import models

#create a vendor model here.
class Vendor(models.Model):
    vendor_name = models.CharField(blank=True, null=True,max_length=100)
    vendor_address = models.CharField(blank=True, null=True,max_length=200)
    vendor_phone = models.CharField(blank=True, null=True,max_length=20)
    vendor_email = models.CharField(blank=True, null=True,max_length=100)
    vendor_notes = models.CharField(blank=True, null=True,max_length=200)
    vendor_services = models.CharField(blank=True, null=True,max_length=200)
    def __str__(self):
        return self.vendor_name

# Create invoices model here.
INVOICE_STATUS_CHOICES = (("quote", "Quote"), ("Requesition", "Requesition"), ("PO", "PO"),("Recieved","Recieved"),("Sent to AP","Sent to AP"), ("paid", "Paid"), ("unpaid", "Unpaid"))
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=10)
    invoice_date = models.DateField(blank=True, null=True)
    vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    invoice_requesition_no = models.CharField(max_length=10)
    invoice_po_no = models.CharField(max_length=10,blank=True, null=True)
    
    invoice_total = models.IntegerField(blank=True, null=True)
    invoice_shipping = models.IntegerField(blank=True, null=True)
    invoice_tax = models.IntegerField(blank=True, null=True)
    invoice_grand_total = models.IntegerField(blank=True, null=True)
    invoice_status = models.CharField(choices=INVOICE_STATUS_CHOICES,max_length=50)
    def __str__(self):
        return self.invoice_number
    def __save__(self):
        self.invoice_grand_total = self.invoice_total + self.invoice_shipping + self.invoice_tax
        super(Invoice, self).save()
