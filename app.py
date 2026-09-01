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
    
    uploaded_file = st.file_uploader("📂 اختر صورة من جهازك", type=["jpg", "png", "jpeg"])
    resolution = st.radio("اختر الدقة المطلوبة:", ["4K Ultra HD", "8K Extreme Detail"])
    
    if st.button("✨ تحسين الصورة الآن"):
        if uploaded_file is None:
            st.warning("يرجى رفع صورة أولاً!")
        else:
            # هنا قمنا ببناء الواجهة التفاعلية بالكامل
            # ملاحظة: سنحتاج لاحقاً لربط هذا الزر بـ API متخصص بالصور (مثل Replicate)
            with st.spinner("جاري تحليل تفاصيل الصورة ومعالجتها..."):
                time.sleep(3) # محاكاة لعملية التحميل
                st.info("الواجهة جاهزة وتعمل بنجاح! لكي يتم تحسين الصورة فعلياً وإرجاعها للمستخدم، نحتاج إلى دمج API خاص بمعالجة الصور في الخطوة القادمة.")
