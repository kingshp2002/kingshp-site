document.addEventListener('DOMContentLoaded', () => {
    // Bootstrap handles the responsive navigation.
    // Keep anchor navigation smooth without breaking normal Django URLs.
    document.querySelectorAll('a[href*="#"]').forEach(link => {
        link.addEventListener('click', event => {
            const url = new URL(link.href, window.location.href);
            if (url.pathname === window.location.pathname && url.hash) {
                const target = document.querySelector(url.hash);
                if (target) {
                    event.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });
});

(function(){
const T={"خانه":"Home","درباره من":"About","مهارت‌ها":"Skills","تجربه":"Experience","پروژه‌ها":"Projects","بلاگ":"Blog","تماس با من":"Contact","ورود":"Login","ثبت‌نام":"Register","خروج":"Logout","مدیریت":"Admin","ادامه مطلب":"Read More","مشاهده پروژه":"View Project","مشاهده مقاله":"Read Article","ارسال":"Submit","ذخیره":"Save","ویرایش":"Edit","حذف":"Delete","دسته‌بندی":"Category","نویسنده":"Author","بازدید":"Views","لایک":"Like","نظرات":"Comments","تماس":"Contact","مهارت‌های من":"My Skills","تجربه کاری":"Experience","درباره":"About","یادگیری":"Learning","مقاله جدید":"New Post"};
const R=Object.fromEntries(Object.entries(T).map(x=>[x[1],x[0]]));
function lang(x){
document.documentElement.lang=x;document.documentElement.dir=x==="en"?"ltr":"rtl";localStorage.setItem("site-language",x);
const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;
while(n=w.nextNode()){let s=n.nodeValue.trim();if(!s||s.length>100)continue;if(x==="en"&&T[s])n.nodeValue=n.nodeValue.replace(s,T[s]);else if(x==="fa"&&R[s])n.nodeValue=n.nodeValue.replace(s,R[s]);}
document.querySelectorAll(".language-switcher [data-lang]").forEach(a=>{a.classList.toggle("btn-warning",a.dataset.lang===x);a.classList.toggle("btn-outline-secondary",a.dataset.lang!==x)});
}
function theme(x){document.documentElement.dataset.theme=x;localStorage.setItem("site-theme",x);let i=document.getElementById("themeIcon");if(i)i.className=x==="dark"?"ri-sun-line":"ri-moon-line";}
document.addEventListener("DOMContentLoaded",()=>{
theme(localStorage.getItem("site-theme")||"light");
document.getElementById("themeToggle")?.addEventListener("click",()=>theme(document.documentElement.dataset.theme==="dark"?"light":"dark"));
lang(localStorage.getItem("site-language")||"fa");
document.querySelectorAll(".language-switcher [data-lang]").forEach(a=>a.addEventListener("click",()=>lang(a.dataset.lang)));
});
})();
