import streamlit as st
import google.generativeai as genai
import urllib.parse
import requests

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

# --- تقسيم الموقع إلى 3 أقسام ---
st.title("🎬 أدوات الإنتاج الاحترافية")
tab1, tab2, tab3 = st.tabs(["📝 مهندس النصوص", "🎨 توليد الصور", "🔍 محسن الصور (مفتوح المصدر)"])

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
                اكتب لي سيناريو للنصوص التي يجب إضافتها على الشاشة لهذه الفكرة: {idea}
                1. 🪝 Hook: جملة افتتاحية قوية لأول 3 ثوانٍ.
                2. ⏱️ السيناريو: العبارات التي ستظهر على الشاشة بالترتيب.
                3. 📝 الوصف: وصف جذاب للمقطع مع هاشتاجات.
                """
                with st.spinner("جاري التخطيط وتوليد النصوص..."):
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال: {e}")

# --- القسم الثاني: صانع الصور (بدون مفتاح) ---
with tab2:
    st.header("توليد صور غلاف بالذكاء الاصطناعي")
    st.write("اكتب وصفاً، وسيقوم الذكاء الاصطناعي برسمه فوراً (مفتوح المصدر وبدون مفتاح).")
    
    image_prompt = st.text_input("🎨 صف الصورة التي تريدها:", "مثال: شخصية مقاتل في لعبة نجاة، جودة 4K")
    
    if st.button("✨ رسم الصورة الآن"):
        if not image_prompt:
            st.warning("يرجى كتابة وصف للصورة أولاً!")
        else:
            with st.spinner("جاري رسم الصورة..."):
                try:
                    safe_prompt = urllib.parse.quote(image_prompt)
                    image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1280&height=720&nologo=true"
                    st.success("🎉 تم رسم الصورة بنجاح!")
                    st.image(image_url, caption=image_prompt)
                    st.markdown(f"[📥 اضغط هنا لتحميل الصورة]({image_url})")
                except Exception as e:
                    st.error(f"فشل الاتصال: {e}")

# --- القسم الثالث: محسن الصور (Hugging Face) ---
with tab3:
    st.header("تحسين جودة الصور (Hugging Face)")
    st.write("نستخدم النماذج المفتوحة المصدر لتحسين دقة الصور. ستحتاج إلى مفتاح Hugging Face المجاني.")
    
    hf_api_key = st.text_input("🔑 أدخل مفتاح Hugging Face الخاص بك:", type="password", key="hf_key")
    uploaded_file = st.file_uploader("📂 اختر صورة من جهازك", type=["jpg", "png", "jpeg"])
    
    if st.button("✨ تحسين دقة الصورة"):
        if not hf_api_key:
            st.warning("يرجى إدخال مفتاح Hugging Face أولاً!")
        elif uploaded_file is None:
            st.warning("يرجى رفع صورة أولاً!")
        else:
            with st.spinner("جاري معالجة الصورة (قد يستغرق الأمر بعض الوقت للنماذج المجانية)..."):
                try:
                    # استخدام نموذج مفتوح المصدر لتحسين الصور (Swin2SR)
                    API_URL = "https://api-inference.huggingface.co/models/caidas/swin2SR-classical-sr-x2-64"
                    headers = {"Authorization": f"Bearer {hf_api_key.strip()}"}
                    
                    response = requests.post(API_URL, headers=headers, data=uploaded_file.getvalue())
                    
                    if response.status_code == 200:
                        st.success("🎉 تم تحسين الصورة بنجاح!")
                        st.image(response.content, caption="الصورة المحسنة")
                        st.download_button(
                            label="📥 تحميل الصورة المحسنة",
                            data=response.content,
                            file_name="upscaled_image.png",
                            mime="image/png"
                        )
                    else:
                        st.error("النموذج قيد التحميل حالياً (جاري تشغيله على الخادم المجاني)، يرجى المحاولة مرة أخرى بعد دقيقة.")
                except Exception as e:
                    st.error(f"فشل الاتصال بالخادم: {e}")
