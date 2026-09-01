import streamlit as st
import google.generativeai as genai
st.markdown(<meta name="google-site-verification" content="eDEfflmb_eJFg-lrhplE3RA_KA_rLP-Pgw0n4IMa0E8" />)
st.set_page_config(page_title="استوديو النصوص الاحترافي", page_icon="✍️", layout="centered")
st.markdown(<meta name="google-site-verification" content="eDEfflmb_eJFg-lrhplE3RA_KA_rLP-Pgw0n4IMa0E8" />)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# ⚠️ ضع مفتاح Gemini API الخاص بك هنا مباشرة ليعمل الموقع تلقائياً دون إزعاج المستخدمين
API_KEY_DEFAULT = "ضع_مفتاحك_هنا"

# --- تقسيم الموقع لأدوات نصية احترافية ---
st.title("✍️ استوديو النصوص الاحترافي")
tab1, tab2, tab3 = st.tabs(["📝 سيناريو المقطع", "🔥 العناوين الفيروسية", "📌 الوصف والهاشتاجات"])

# --- القسم الأول: كتابة السيناريو الاحترافي ---
with tab1:
    st.header("هندسة سيناريوهات الفيديوهات القصيرة")
    
    col1, col2 = st.columns(2)
    with col1:
        platform = st.selectbox("📱 المنصة المستهدفة:", ["TikTok", "YouTube Shorts", "Instagram Reels"])
    with col2:
        tone = st.selectbox("🎭 أسلوب الكتابة:", ["🔥 حماسي وسريع (أكشن)", "🤔 غامض ومثير للفضول", "😂 كوميدي وساخر", "👔 احترافي وتعليمي"])
        
    idea = st.text_area("💡 ما هي فكرة المقطع؟", "مثال: لقطة قنص أسطورية في فري فاير ونهاية غير متوقعة")
    
    if st.button("🚀 كتابة السيناريو الاحترافي"):
        if not idea:
            st.warning("يرجى كتابة الفكرة!")
        else:
            try:
                genai.configure(api_key=API_KEY_DEFAULT)
                model = genai.GenerativeModel('gemini-3.6-flash')
                prompt = f"""
                أنت خبير في كتابة سيناريوهات الفيديوهات القصيرة سريعة الانتشار (Viral).
                اكتب لي سيناريو لنصوص الشاشة (Text Overlays) لفيديو سيُنشر على {platform}.
                فكرة الفيديو: {idea}
                الأسلوب المطلوب: {tone}
                
                يجب أن يكون الرد مقسماً باحترافية كالتالي:
                1. 🪝 الخطاف (The Hook): عبارة صادمة أو مثيرة للفضول تظهر في أول ثانيتين لتمنع المشاهد من التمرير.
                2. 🎬 التسلسل النصي: العبارات التي ستظهر على الشاشة بالترتيب الزمني (مثال: الثانية 3: النص... ، الثانية 5: النص...). يجب أن تكون الكلمات قصيرة، قوية، ومناسبة للأسلوب المختار.
                3. 💥 الخاتمة (Call to Action): طلب ذكي للمتابعة أو التفاعل في نهاية المقطع.
                """
                with st.spinner("جاري صياغة السيناريو باحترافية..."):
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

# --- القسم الثاني: توليد العناوين ---
with tab2:
    st.header("صانع العناوين الفيروسية (Clickbait)")
    st.write("احصل على عناوين تجبر المشاهد على النقر ومشاهدة المقطع.")
    
    title_idea = st.text_input("🎯 عن ماذا يتحدث المقطع؟", "مثال: تحدي ون شوت في لعبة باتل رويال")
    
    if st.button("💡 توليد 5 عناوين"):
        if not title_idea:
            st.warning("يرجى كتابة موضوع المقطع!")
        else:
            try:
                genai.configure(api_key=API_KEY_DEFAULT)
                model = genai.GenerativeModel('gemini-3.6-flash')
                prompt = f"""
                أنت خبير في التسويق وكتابة العناوين الجذابة (Clickbait) على يوتيوب وتيك توك.
                اقترح لي 5 عناوين قصيرة، قوية جداً، ومثيرة للفضول لهذا الموضوع: {title_idea}
                لا تستخدم لغة معقدة، اجعلها لغة قريبة من الشباب واللاعبين، واستخدم الإيموجي المناسب.
                """
                with st.spinner("جاري توليد العناوين..."):
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

# --- القسم الثالث: الوصف والهاشتاجات ---
with tab3:
    st.header("خبير الـ SEO (لزيادة المشاهدات)")
    desc_idea = st.text_area("📝 اكتب فكرة الفيديو لاستخراج الكلمات المفتاحية:", "مثال: لقطات لعب قوية وتكتيكات للفوز للوصول لرانك عالي")
    
    if st.button("🔍 تجهيز الوصف والهاشتاجات"):
        if not desc_idea:
            st.warning("يرجى كتابة الفكرة!")
        else:
            try:
                genai.configure(api_key=API_KEY_DEFAULT)
                model = genai.GenerativeModel('gemini-3.6-flash')
                prompt = f"""
                أنت خبير في خوارزميات البحث (SEO) للمنصات الاجتماعية.
                لدي فيديو فكرته: {desc_idea}
                
                اكتب لي:
                1. 📝 وصفاً قصيراً وجذاباً للفيديو (سطرين كحد أقصى) يحتوي على كلمات مفتاحية قوية بأسلوب طبيعي.
                2. 🏷️ قائمة بأفضل 10 هاشتاجات (Trending) لتصدر نتائج البحث في هذا المجال.
                """
                with st.spinner("جاري تحليل الخوارزميات..."):
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

import streamlit as st

st.set_page_config(page_title="Lexisynth - استوديو النصوص", page_icon="✍️", layout="centered")

# كود إثبات الملكية لجوجل
st.markdown(<meta name="google-site-verification" content="eDEfflmb_eJFg-lrhplE3RA_KA_rLP-Pgw0n4IMa0E8" />)
