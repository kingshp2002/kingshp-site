from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=200, verbose_name="موضوع")
    message = models.TextField(verbose_name="متن پیام")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان پروژه")
    description = models.TextField(verbose_name="توضیحات پروژه")
    image = models.ImageField(upload_to='static/portfolio_images/', verbose_name="تصویر پروژه")
    github_link = models.URLField(blank=True, null=True, verbose_name="لینک گیت‌هاب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"
        ordering = ['-created_at']

    def __str__(self):
        return self.title