import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="مهندس المقاطع الصامتة (النسخة الاحترافية)", page_icon="🎮", layout="centered")

# --- نظام تسجيل الدخول والاشتراكات ---
st.sidebar.title("🔐 تسجيل الدخول")
st.sidebar.write("هذه الأداة مدفوعة للمشتركين فقط.")
user_password = st.sidebar.text_input("أدخل كود الاشتراك الخاص بك:", type="password")

valid_passwords = ["aboshalool_vip", "pro_user_2026", "freefire_king"]

if user_password not in valid_passwords:
    st.title("🎬 مُهندس الفيديوهات القصيرة الصامتة")
    st.warning("عذراً، يجب إدخال كود اشتراك صالح في القائمة الجانبية لاستخدام الأداة.")
    st.info("للحصول على كود اشتراك، يمكنك زيارة متجرنا.")
    st.stop()

st.sidebar.success("تم التحقق بنجاح!")

# --- تقسيم الموقع إلى قسمين (تبويبات) ---
st.title("🎬 أدوات الإنتاج الاحترافية")
tab1, tab2 = st.tabs(["📝 مهندس النصوص (السيناريو)", "🖼️ محسن الصور (4K/8K)"])

# --- القسم الأول: مهندس النصوص ---
with tab1:
    st.header("توليد سيناريوهات المقاطع")
    api_key = st.text_input("🔑 أدخل مفتاح Gemini API الخاص بك:", type="password", key="gemini_key")
    idea = st.text_area("💡 ما هي فكرة المقطع الذي سجلته؟", "مثال: لقطة قنص أسطورية...")
    
    if st.button("🚀 توليد خطة المقطع"):
        if not api_key:
            st.warning("يرجى إدخال مفتاح الـ API أولاً!")
        elif not idea:
            st.warning("يرجى كتابة فكرة المقطع!")
        else:
            try:
                genai.configure(api_key=api_key.strip())
                model = genai.GenerativeModel('gemini-3.6-flash')
                prompt = f"""
                أنا صانع محتوى أنشر مقاطع قصيرة تعتمد على تسجيل الشاشة فقط بدون تعليق صوتي.
                اكتب لي سيناريو للنصوص التي يجب إضافتها على الشاشة (Text Overlays) لهذه الفكرة: {idea}
                
                أريد التقسيم التالي:
                1. 🪝 Hook: جملة افتتاحية قوية جداً لأول 3 ثوانٍ.
                2. ⏱️ السيناريو: العبارات التي ستظهر على الشاشة بالترتيب مع التوقيت.
                3. 📝 الوصف: وصف جذاب للمقطع مع هاشتاجات قوية للانتشار.
                """
                with st.spinner("جاري التخطيط وتوليد النصوص..."):
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال: {e}")

# --- القسم الثاني: محسن الصور ---
with tab2:
    st.header("رفع دقة الصور المصغرة بالذكاء الاصطناعي")
    st.write("قم برفع لقطة شاشة من اللعب، وسنقوم بتحسين جودتها لتصبح جاهزة كغلاف للمقطع.")
    
    # مفتاح API الخاص بالصور
    image_api_key = st.text_input("🔑 أدخل مفتاح DeepAI API الخاص بك:", type="password")
    
    uploaded_file = st.file_uploader("📂 اختر صورة من جهازك", type=["jpg", "png", "jpeg"])
    
    import requests # مكتبة الاتصال بالخوادم
    
    if st.button("✨ تحسين الصورة الآن"):
        if not image_api_key:
            st.warning("يرجى إدخال مفتاح الـ API الخاص بالصور أولاً!")
        elif uploaded_file is None:
            st.warning("يرجى رفع صورة أولاً!")
        else:
            with st.spinner("جاري تحليل تفاصيل الصورة ومعالجتها (قد يستغرق بضع ثوانٍ)..."):
                try:
                    # إرسال الصورة لخوادم DeepAI لتحسين الدقة
                    response = requests.post(
                        "https://api.deepai.org/api/torch-srgan",
                        files={
                            'image': uploaded_file.getvalue(),
                        },
                        headers={'api-key': image_api_key.strip()}
                    )
                    
                    data = response.json()
                    
                    if 'output_url' in data:
                        st.success("🎉 تم تحسين الصورة بنجاح!")
                        # عرض الصورة المحسنة
                        st.image(data['output_url'], caption="الصورة بالدقة العالية")
                        
                        # زر تحميل الصورة
                        st.markdown(f"[📥 اضغط هنا لتحميل الصورة بدقتها الكاملة]({data['output_url']})")
                    else:
                        st.error("حدث خطأ أثناء معالجة الصورة. تأكد من صلاحية المفتاح.")
                        
                except Exception as e:
                    st.error(f"فشل الاتصال بالخادم: {e}")محاكاة لعملية التحميل
                st.info("الواجهة جاهزة وتعمل بنجاح! لكي يتم تحسين الصورة فعلياً وإرجاعها للمستخدم، نحتاج إلى دمج API خاص بمعالجة الصور في الخطوة القادمة.")
