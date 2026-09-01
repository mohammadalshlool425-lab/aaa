import streamlit as st
import google.generativeai as genai

# إعدادات شكل الصفحة
st.set_page_config(page_title="مهندس المقاطع الصامتة", page_icon="🎮", layout="centered")

# العناوين
st.title("🎬 مُهندس الفيديوهات القصيرة الصامتة")
st.write("اكتب فكرة المقطع، وسأقوم بتوليد سيناريو كامل للكلمات التي يجب أن تكتبها على الشاشة لجذب المشاهدين، بدون الحاجة لأي تعليق صوتي.")

# إدخال مفتاح الـ API
api_key = st.secrets[ "GEMINI_API_KEY"]

# مربع فكرة الفيديو
idea = st.text_area("💡 ما هي فكرة المقطع الذي سجلته؟", "مثال: لقطة قنص أسطورية في فري فاير مع حركة سريعة")

# زر التشغيل
if st.button("🚀 توليد خطة المقطع"):
    if not api_key:
        st.warning("يرجى إدخال مفتاح الـ API أولاً!")
    elif not idea:
        st.warning("يرجى كتابة فكرة المقطع!")
    else:
        try:
            # ربط الكود بـ API
            genai.configure(api_key=api_key.strip())
            
            # استخدام النموذج الأحدث المطلوب من الخادم مباشرة
            model = genai.GenerativeModel('gemini-3.6-flash')
            
            # نص الطلب
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
                st.success("تم توليد خطة المقطع بنجاح!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال: {e}")
