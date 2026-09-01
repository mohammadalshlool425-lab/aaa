import streamlit as st
import google.generativeai as genai

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

# --- تحسين ذكي: مفتاح API واحد يُشغّل الموقع بالكامل ---
st.sidebar.markdown("---")
st.sidebar.write("⚙️ إعدادات الذكاء الاصطناعي")
api_key = st.sidebar.text_input("🔑 أدخل مفتاح Gemini API الخاص بك:", type="password")

# --- تقسيم الموقع ---
st.title("🎬 أدوات الإنتاج الاحترافية")
tab1, tab2, tab3 = st.tabs(["📝 مهندس النصوص", "🎨 توليد الصور (Google)", "🔍 البوابة الذكية للصور"])

# --- القسم الأول: مهندس النصوص ---
with tab1:
    st.header("توليد سيناريوهات المقاطع")
    idea = st.text_area("💡 ما هي فكرة المقطع الذي سجلته؟", "مثال: لقطة قنص أسطورية مع حركة سريعة")
    
    if st.button("🚀 توليد خطة المقطع"):
        if not api_key:
            st.warning("يرجى إدخال مفتاح الـ API في القائمة الجانبية أولاً!")
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

# --- القسم الثاني: صانع الصور (Imagen من Google) ---
with tab2:
    st.header("توليد صور غلاف احترافية (Google Imagen 3)")
    st.write("استخدمنا نماذج جوجل الرسمية للصور لتوليد أغلفة بمقاس اليوتيوب (16:9) باستخدام نفس مفتاح Gemini.")
    
    image_prompt = st.text_input("🎨 صف الصورة التي تريدها:", "مثال: شخصية مقاتل في ساحة المعركة، إضاءة سينمائية، جودة عالية")
    
    if st.button("✨ رسم الصورة عبر Google"):
        if not api_key:
            st.warning("يرجى إدخال مفتاح الـ API في القائمة الجانبية أولاً!")
        elif not image_prompt:
            st.warning("يرجى كتابة وصف للصورة أولاً!")
        else:
            with st.spinner("جاري رسم الصورة عبر خوادم جوجل..."):
                try:
                    genai.configure(api_key=api_key.strip())
                    # استخدام نموذج الصور الرسمي من جوجل
                    image_model = genai.ImageGenerationModel("imagen-3.0-generate-001")
                    
                    result = image_model.generate_images(
                        prompt=image_prompt,
                        number_of_images=1,
                        aspect_ratio="16:9" # مقاس مثالي لليوتيوب والشاشات
                    )
                    
                    st.success("🎉 تم رسم الصورة بنجاح!")
                    
                    for generated_image in result.images:
                        st.image(generated_image.image, caption=image_prompt)
                        
                except Exception as e:
                    st.error(f"حدث خطأ أثناء الرسم: {e}")
                    st.info("ملاحظة: إذا ظهر لك خطأ هنا، فقد تكون ميزة توليد الصور غير مفعلة بعد في حسابك على Google AI Studio للمنطقة التي تتواجد بها.")

# --- القسم الثالث: البوابة الذكية للصور ---
with tab3:
    st.header("تحسين جودة الصور إلى 4K و 8K")
    st.write("البوابة السريعة لأدوات تحسين جودة الصور المفتوحة المصدر.")
    st.info("💡 اختر الأداة التي تناسبك:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🚀 تحسين الصور (أداة CodeFormer)", "https://huggingface.co/spaces/sczhou/CodeFormer", use_container_width=True)
    with col2:
        st.link_button("✨ تحسين الصور (أداة Upscayl)", "https://huggingface.co/spaces/doevent/upscayl", use_container_width=True)
