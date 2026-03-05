import re

with open('landing_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Alpine.js to <head>
alpine_script = '    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>'
if alpine_script not in html:
    html = html.replace('</head>', f'{alpine_script}\n</head>')

# 2. Add the Video Section between About and Services
# We will embed the Instagram Reel using an iframe since Instagram doesn't provide raw .mp4 easily
video_section = """
    <!-- Video Section -->
    <section class="py-24 px-6 md:px-12 bg-background-dark text-white relative overflow-hidden" id="video-tour" data-aos="fade-up">
        <div class="absolute inset-0 z-0 opacity-20">
            <div class="w-full h-full bg-cover bg-center" style="background-image: url('pilates_classico.png');"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/80 to-background-dark"></div>
        </div>
        
        <div class="relative z-10 max-w-7xl mx-auto flex flex-col items-center text-center">
            <span class="text-primary font-medium tracking-widest text-sm uppercase block mb-4">Conheça nosso espaço</span>
            <h2 class="text-4xl md:text-5xl font-display font-medium mb-12">Um Tour pelo Studio RL</h2>
            
            <!-- Modal video component -->
            <div class="[&_[x-cloak]]:hidden" x-data="{ modalOpen: false }">
                <!-- Video thumbnail -->
                <button class="relative flex justify-center items-center focus:outline-none focus-visible:ring focus-visible:ring-primary rounded-3xl group" @click="modalOpen = true" aria-controls="modal" aria-label="Watch the video">
                    <img class="rounded-3xl shadow-2xl transition-transform duration-500 ease-in-out group-hover:scale-[1.02] border border-white/10" src="pilates_classico.png" width="768" height="432" alt="Studio Video Thumbnail" style="height: 400px; object-fit: cover;" />
                    <div class="absolute inset-0 bg-black/40 rounded-3xl group-hover:bg-black/30 transition-colors duration-500"></div>
                    <!-- Play icon -->
                    <svg class="absolute pointer-events-none group-hover:scale-110 transition-transform duration-300 ease-in-out" xmlns="http://www.w3.org/2000/svg" width="80" height="80">
                        <circle class="fill-black/50 backdrop-blur-md" cx="40" cy="40" r="40" />
                        <path class="fill-primary drop-shadow-2xl" d="M48 40a.999.999 0 0 0-.427-.82l-12-8A1 1 0 0 0 34 32v16a.999.999 0 0 0 1.573.82l12-8A.995.995 0 0 0 48 40Z" />
                    </svg>
                </button>

                <!-- Modal backdrop -->
                <div class="fixed inset-0 z-[110] bg-black bg-opacity-80 backdrop-blur-sm transition-opacity" x-show="modalOpen" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="transition ease-out duration-200" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" aria-hidden="true" x-cloak></div>

                <!-- Modal dialog -->
                <div id="modal" class="fixed inset-0 z-[120] flex px-4 md:px-6 py-6" role="dialog" aria-modal="true" x-show="modalOpen" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 scale-95" x-transition:enter-end="opacity-100 scale-100" x-transition:leave="transition ease-out duration-200" x-transition:leave-start="opacity-100 scale-100" x-transition:leave-end="opacity-0 scale-95" x-cloak>
                    <div class="max-w-4xl mx-auto h-full flex items-center justify-center w-full">
                        <div class="w-full relative rounded-3xl shadow-2xl bg-black overflow-hidden flex justify-center" @click.outside="modalOpen = false" @keydown.escape.window="modalOpen = false" style="max-height: 90vh;">
                            <button class="absolute top-4 right-4 z-20 w-10 h-10 bg-black/50 hover:bg-black/80 text-white rounded-full flex items-center justify-center backdrop-blur-md transition-colors" @click="modalOpen = false">
                                <span class="material-symbols-outlined">close</span>
                            </button>
                            
                            <!-- Instagram Embedded Reel -->
                            <div class="w-full flex justify-center bg-black py-4">
                                <iframe class="instagram-media instagram-media-rendered" id="instagram-embed-0" src="https://www.instagram.com/reel/C2-lE58OQ7w/embed/?autoplay=1" allowtransparency="true" allowfullscreen="true" frameborder="0" height="700" data-instgrm-payload-id="instagram-media-payload-0" scrolling="no" style="background: white; max-width: 400px; width: calc(100% - 2px); border-radius: 3px; border: 1px solid #dbdbdb; box-shadow: none; display: block; margin: 0px; min-width: 326px; padding: 0px;"></iframe>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Instagram provided link was https://www.instagram.com/reel/DU8m2gJkfrW/\?utm_source\=ig_web_copy_link\&igsh\=MzRlODBiNWFlZA\=\=
# The shortcode is DU8m2gJkfrW. Changing embed src to reflect it.
video_section = video_section.replace('C2-lE58OQ7w', 'DU8m2gJkfrW')

# Find exactly where to insert: between About and Services
# Look for <!-- Services Section -->
html = html.replace('    <!-- Services Section -->', video_section + '\n    <!-- Services Section -->')

with open('landing_page.html', 'w', encoding='utf-8') as f:
    f.write(html)
