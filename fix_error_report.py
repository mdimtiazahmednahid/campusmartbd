import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_catch = '''        .catch((error) => {
            showToast('There was an issue submitting your order. Please try again.'); reportError('Order submission failed', 'form_submit');
        })'''

new_catch = '''        .catch((error) => {
            const container = document.getElementById('toast-container');
            if (container) {
                const toast = document.createElement('div');
                toast.className = `toast toast-error`;
                const toastId = 'toast-' + Date.now();
                toast.innerHTML = `<span style="font-size: 1.2rem;">⚠️</span> 
                                   <span style="display:flex; flex-direction:column; gap:0.5rem; width:100%;">
                                       <span>Order submission failed. Please try again.</span>
                                       <button id="btn-${toastId}" style="background:rgba(255,255,255,0.2); color:white; border:1px solid rgba(255,255,255,0.4); padding:0.4rem 0.8rem; border-radius:6px; cursor:pointer; font-weight:600; font-size:0.8rem; transition:all 0.2s; align-self:flex-start;">Send Error Report</button>
                                   </span>`;
                container.appendChild(toast);
                setTimeout(() => toast.classList.add('show'), 10);
                
                const btn = document.getElementById(`btn-${toastId}`);
                if (btn) {
                    btn.addEventListener('click', (e) => {
                        e.target.textContent = 'Sending...';
                        e.target.style.opacity = '0.7';
                        reportError('Order submission failed', 'form_submit');
                        setTimeout(() => { 
                            e.target.textContent = 'Report Sent!'; 
                            e.target.style.background = 'rgba(16, 185, 129, 0.3)'; 
                            e.target.style.borderColor = 'rgba(16, 185, 129, 0.8)';
                            e.target.style.opacity = '1';
                        }, 800);
                    });
                }
                
                setTimeout(() => {
                    toast.classList.remove('show');
                    setTimeout(() => toast.remove(), 300);
                }, 6000);
            }
        })'''

js = js.replace(old_catch, new_catch)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Fixed error reporting")
