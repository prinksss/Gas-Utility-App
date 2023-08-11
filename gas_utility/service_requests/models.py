from django.db import models

class ServiceRequest(models.Model):
    TYPES = (
        ('Gas Leak', 'Gas Leak'),
        ('Appliance Repair', 'Appliance Repair'),
        ('Meter Installation', 'Meter Installation'),
    
    )
    
    customer_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=50, choices=TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='service_request_attachments/', null=True, blank=True)
    submitted_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.customer_name} - {self.request_type}"
