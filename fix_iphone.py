import re

with open('landing_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Novo estilo da div do iPhone:
# Precisamos fazer um replace mais seguro que não falhe (a div extra de inner bezel).

old_wrapper_pattern = r'<!-- iPhone Mockup Frame -->\s*<div class="relative w-full max-w-\[360px\].*?<!-- Inner Bezel & Screen/Iframe Container -->\s*<div class="absolute inset-0 w-full h-full bg-black rounded-\[2\.8rem\] overflow-hidden flex items-center justify-center p-\[4px\]">\s*<div class="w-full h-full rounded-\[2\.5rem\] overflow-hidden bg-black flex items-center justify-center">'

new_iphone_mockup = """<!-- iPhone Mockup Frame -->
                <div class="relative w-full max-w-[380px] aspect-[9/16] bg-slate-400 rounded-[3.5rem] shadow-[0_30px_70px_rgba(0,0,0,0.6)] border-[14px] border-slate-500 group">
                    
                    <!-- Simples Speaker/Camera (Sem Notch gigante pra não tampar o Header) -->
                    <div class="absolute top-0 inset-x-0 h-4 flex justify-center z-50">
                        <div class="w-16 h-4 bg-slate-800 rounded-b-xl mt-[1px] relative z-20 flex items-center justify-center gap-2">
                            <div class="w-1.5 h-1.5 rounded-full bg-slate-600"></div>
                            <div class="w-6 h-1 rounded-full bg-slate-900 border border-slate-700/50"></div>
                        </div>
                    </div>
                    
                    <!-- Buttons (Left) bg-slate-600 p/ contraste na borda 500 -->
                    <div class="absolute -left-[16px] top-28 w-[2px] h-8 bg-slate-600 rounded-l-md"></div>
                    <div class="absolute -left-[16px] top-40 w-[2px] h-14 bg-slate-600 rounded-l-md"></div>
                    <div class="absolute -left-[16px] top-60 w-[2px] h-14 bg-slate-600 rounded-l-md"></div>
                    
                    <!-- Button (Right) bg-slate-600 -->
                    <div class="absolute -right-[16px] top-40 w-[2px] h-20 bg-slate-600 rounded-r-md"></div>
                    
                    <!-- Inner Bezel & Screen/Iframe Container -->
                    <div class="absolute inset-0 w-full h-full bg-black rounded-[2.8rem] overflow-hidden flex items-center justify-center border-4 border-black">
                        <!-- Sem margens exageradas para caber o iframe 100% -->
                        <div class="w-full h-full rounded-[2.5rem] overflow-hidden bg-white flex items-center justify-center relative">"""

html = re.sub(old_wrapper_pattern, new_iphone_mockup, html, flags=re.DOTALL)

with open('landing_page.html', 'w', encoding='utf-8') as f:
    f.write(html)
