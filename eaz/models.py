from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.title


class Thing(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='things')
    link = models.URLField()
    
    def __str__(self) -> str:
        return self.name


# class Famous(models.Model):
#     name = models.CharField(50)
#     description = models.TextField()


# class Food(models.Model):
#     name = models.CharField(50)
#     description = models.TextField()

# class Place(models.Model):
#     name = models.CharField(50)
#     description = models.TextField()


class Image(models.Model):
    image = models.ImageField(upload_to='image')
    thing = models.ForeignKey(Thing,on_delete=models.CASCADE,related_name='images')
    # famous = models.ForeignKey(Famous,on_delete=models.CASCADE,null=True,blank=True,related_name='images')
    # food = models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True,related_name='images')
    # place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,blank=True,related_name='images')












'''
// export const menu = [
//   { id: 1, title: "خانه", link: "/" },
//   { id: 3, title: "غذاها", link: "/foods" },
//   { id: 4, title: "مشاهیر", link: "/famous" },
//   { id: 2, title: "مکان های گردشگری", link: "/places" },
//   { id: 5, title: "ورود / عضویت", link: "/auth/singIn"}
// ];



export const famous = {
  id: 1,
  title: " مشاهیر آذربایجان شرقی ",
  items: [
    {
      id: 1,
      name: "بابک خرمدین",
      description:
        "بابک خرمدین (درگذشتۀ صفر ۲۲۳ / ژانویۀ ۸۳۸)، رهبر اصلی مبارزان ایرانی علیه سلطه خلافت عباسی و از پیروان جنبش خرمدینان بود که پس از مرگ ابومسلم خراسانی، بر خلافت عباسی شورید. خرمدینان، مرگ ابومسلم را انکار کردند و معتقد بودند که او باز خواهد گشت تا عدالت را در جهان، برقرار کند. در دوران خلافت عباسیان، آذربایجان، کانون مقاومت طولانی‌مدت و خطرناک علیه خلافت بود که توسط بابک خرمدین، رهبری می‌شد و بر شمال غربی ایران، تأثیر گذاشته بود و بیش از ۲۰ سال — از ۲۰۱ ه‍.ق / ۸۱۶ م تا ۲۲۲ ه‍.ق /۸۳۷ م — طول کشید. از نگاه کلیفورد ادموند باسورث، این مقاومت قطعاً پایه‌های دینی داشت اما ممکن است که پایه‌های سیاسی-اجتماعی نیز داشته باشد. شورش او به روشنی از حس ضد عربی ایرانیان در آذربایجان بهره می‌برده‌است تعداد نیروهای لشکر بابک را در ابوالمعالی ۱۰۰ هزار نفر، در تنبیه الاشراف مسعودی ۲۰۰ هزار نفر، در تاریخ بغدادی ۳۰۰ هزار نفر یا بیشمار و در تبصره العوام بیشمار ذکر کرده‌اندکه بی شک مبالغه‌آمیز است ولی حداقل دلالت بر بزرگ بودن لشکر آن دارد.      ",
      images: ["./src/images/babak1_400.jpg", "src/images/babak2.jpg"],
      link: "https://fa.wikipedia.org/wiki/%D8%A8%D8%A7%D8%A8%DA%A9_%D8%AE%D8%B1%D9%85%D8%AF%DB%8C%D9%86",
    },
    {
      id: 2,
      name: "استاد شهریار",
      description:
        "آسیّد محمّدحسین بهجت تبریزی (۱۱ دی ۱۲۸۵ – ۲۷ شهریور ۱۳۶۷) متخلص به شهریار، شاعر ایرانی بود. او اهل تبریز بود و به زبان‌ ترکی آذربایجانی و فارسی شعر سروده‌است. شهریار در سرودن گونه‌های دگرسان شعر مانند قصیده، مثنوی، غزل، قطعه، رباعی و شعر نیمایی چیره‌دست بود . اما بیشتر از دیگر گونه‌ها در غزل شهره بود و از جمله غزل‌های معروف او می‌توان به «علی ای همای رحمت» و «آمدی جانم به قربانت» اشاره کرد. شهریار نسبت به علی بن ابی‌طالب ارادتی ویژه داشت و همچنین شیفتگی بسیاری نسبت به حافظ و فردوسی داشته‌است. او در تبریز در خانواده‌ای بستان‌آبادی از روستای خُشکِناب به دنیا آمد و بنا به وصیتش در مقبرةالشعرای تبریز به خاک سپرده شد. ۲۷ شهریور را به واسطهٔ روز درگذشت او «روز شعر و ادب ملی» نامیده‌اند. مهم‌ترین آثار شهریار به زبان ترکی منظومهٔ حیدربابایه سلام و منظومه سهندیه است که از معروف‌ترین آثار ادبیات ترکی آذربایجانی به‌شمار می‌روند و شاعر در آنها از اصالت و زیبایی‌های روستای دوران کودکیش و کوه سهند یاد کرده‌است",
      images: ["public/images/Shahriyar.jpg", "public/images/Shahriyar1.jpg"],
      link: "https://fa.wikipedia.org/wiki/%D8%B4%D9%87%D8%B1%DB%8C%D8%A7%D8%B1_(%D8%B4%D8%A7%D8%B9%D8%B1)",
    },
    {
      id: 3,
      name: "پروین اعتصامی",
      description:
        "رخشنده اعتصامی (۲۵ اسفندِ ۱۲۸۵ – ۱۵ فروردینِ ۱۳۲۰)، معروف به پروین اعتصامی، شاعر ایرانی بود. او بیشتر به‌دلیل به کار بردن سبک شعریِ مناظره در شعرهایش معروف است. مضامین و معانی شعرهای او توصیف‌کنندهٔ دلبستگیِ عمیقش به پدر، استعداد و شوقِ فراوانش به آموختنِ دانش، روحیهٔ ظلم‌ستیزی و مخالفت با ستم و ستمگران، حمایت از حقوقِ زنان و ابراز همدلی و همدردی با محرومان و ستم‌دیدگان است. او را «مشهورترین شاعر زن ایران» گفته‌اند. اعتصامی از کودکی فارسی و انگلیسی و عربی را نزدِ پدرش آموخت و از همان کودکی زیرِ نظرِ پدر و استادانی چون علی‌اکبر دهخدا و محمّدتقی بهار سرودنِ شعر را آغاز کرد. پدرش، یوسف اعتصامی آشتیانی، شاعر و مترجم بود و در شکل‌گیریِ زندگیِ هنریِ پروین و کشفِ توانایی‌ها و ذوق و گرایشش به شعر نقشِ مهمّی داشت. اعتصامی در بیست‌وهشت‌سالگی ازدواج کرد؛ امّا، به خاطرِ اختلافِ فکری با همسرش، پس از چندی از او جدا شد. پس از جدایی مدّتی در کتابخانهٔ دانشسرای عالی تهران به کتابداری مشغول شد. یگانه اثرِ چاپ و منتشرشده از پروین دیوانِ اشعار اوست، که دارای ۶۰۶ شعر شامل اشعاری در قالب‌های مثنوی، قطعه و قصیده است.
        '''