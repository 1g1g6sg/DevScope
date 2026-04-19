import requests
import matplotlib.pyplot as plt
from collections import Counter

def analyze_github(username):
    print(f"\n🔍 تحليل حساب: {username}\n")
    
    # جلب بيانات المستخدم
    user = requests.get(f"https://api.github.com/users/{username}").json()
    repos = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100").json()
    
    print(f"👤 الاسم: {user.get('name', 'غير محدد')}")
    print(f"📦 عدد المستودعات: {user.get('public_repos', 0)}")
    print(f"⭐ المتابعون: {user.get('followers', 0)}")
    print(f"📍 الموقع: {user.get('location', 'غير محدد')}")
    
    # أكثر لغة مستخدمة
    languages = [r['language'] for r in repos if r.get('language')]
    lang_count = Counter(languages)
    
    if lang_count:
        print(f"\n💻 أكثر لغة: {lang_count.most_common(1)[0][0]}")
    else:
        print("\n💻 أكثر لغة: لا توجد")
    
    # النجوم الكلية
    total_stars = sum(r.get('stargazers_count', 0) for r in repos)
    print(f"⭐ إجمالي النجوم: {total_stars}")
    
    # رسم بياني
    if lang_count:
        langs = list(lang_count.keys())[:5]
        counts = [lang_count[l] for l in langs]
        
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.bar(langs, counts, color='steelblue')
        plt.title(f'اللغات - {username}')
        plt.xlabel('اللغة')
        plt.ylabel('عدد المستودعات')
        
        plt.subplot(1, 2, 2)
        plt.pie(counts, labels=langs, autopct='%1.1f%%')
        plt.title('نسبة اللغات')
        
        plt.tight_layout()
        plt.savefig(f'{username}_analysis.png')
        plt.show()
        print(f"\n✅ تم حفظ الرسم البياني كـ {username}_analysis.png")
    else:
        print("\n⚠️ لا توجد لغات لعرضها")

# تشغيل الأداة
username = input("أدخل اسم المستخدم في GitHub: ")
analyze_github(username)