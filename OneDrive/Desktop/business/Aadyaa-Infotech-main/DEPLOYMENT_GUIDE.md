# 🎯 Quick Start - Deploy to GoDaddy

## ✅ Pre-Deployment Checklist

### 1. Update Contact Info (REQUIRED)
**Files to edit:**
- `index.html` (lines 57, 136)
- `src/components/SEO.jsx` (lines 48, 95)

**Replace:**
- Phone: `+91-XXXXXXXXXX` → Your actual number
- Email: `info@aadyaainfotech.in` → Your actual email
- Social media links → Your profiles

### 2. Build Production Version
```bash
npm run build
```
✅ Build successful! Files are in `dist/` folder

---

## 🚀 Upload to GoDaddy

### Method 1: cPanel File Manager (Easiest)

1. **Login to GoDaddy cPanel**
   - Go to: https://mya.godaddy.com/
   - Click "cPanel Admin"

2. **Open File Manager**
   - Navigate to: `public_html` folder
   - Delete default files (if any)

3. **Upload Files**
   - Upload ALL contents of `dist` folder
   - NOT the `dist` folder itself, but its contents
   - Files should go directly into `public_html`

4. **Verify Upload**
   - Should have: `index.html`, `assets/` folder, etc.
   - Visit: https://aadyaainfotech.in/

### Method 2: FTP (FileZilla)

1. **Get FTP Credentials from GoDaddy**
   - Hosting → Manage → FTP Access
   - Note: Host, Username, Password

2. **Connect with FileZilla**
   - Host: Your domain or IP
   - Username: From GoDaddy
   - Password: From GoDaddy
   - Port: 21

3. **Upload**
   - Local: Select all files from `dist` folder
   - Remote: `/public_html/`
   - Transfer all files

---

## 🔍 Post-Deployment Actions

### 1. Test Website
- [ ] Homepage loads correctly
- [ ] All sections visible
- [ ] Images loading
- [ ] Forms working (if any)
- [ ] Mobile responsive
- [ ] Dark mode working

### 2. Submit to Search Engines

**Google Search Console:**
1. Go to: https://search.google.com/search-console
2. Add property: `aadyaainfotech.in`
3. Verify ownership (DNS method recommended)
4. Submit sitemap: `https://aadyaainfotech.in/sitemap.xml`

**Bing Webmaster Tools:**
1. Go to: https://www.bing.com/webmasters
2. Add site
3. Verify ownership
4. Submit sitemap

### 3. Google My Business
1. Visit: https://www.google.com/business/
2. Create business profile
3. Add:
   - Business name: "Aadyaa Infotech"
   - Address: Ahmedabad, Gujarat
   - Phone: Your number
   - Website: https://aadyaainfotech.in/
   - Category: "Web Design Company" / "Digital Marketing Agency"
4. Verify by postcard (takes 5-7 days)

### 4. Install Analytics (Optional but Recommended)

**Google Analytics 4:**
1. Create account: https://analytics.google.com/
2. Get Measurement ID (starts with G-)
3. Create `public/analytics.js`:
```javascript
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-XXXXXXXXXX');
```
4. Add to `index.html` before `</head>`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script async src="/analytics.js"></script>
```
5. Rebuild: `npm run build`
6. Re-upload to GoDaddy

---

## 📱 Social Media Setup

Create profiles on:
- Facebook: https://facebook.com/pages/create
- Instagram: @aadyaainfotech
- LinkedIn: https://linkedin.com/company
- Twitter: @aadyaainfotech

Add website link: https://aadyaainfotech.in/

---

## 🎯 Local Directories (India Specific)

List your business on:
- JustDial
- IndiaMART
- Sulekha
- TradeIndia
- AskLaila
- HotFrog India

---

## ⚡ Performance Tips

### Image Optimization
Compress images before upload:
- Use: TinyPNG.com or Squoosh.app
- Recommended format: WebP
- Max file size: < 100KB per image

### Enable Compression
Add `.htaccess` file to root:
```apache
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript
</IfModule>
```

### Browser Caching
Add to `.htaccess`:
```apache
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpg "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/gif "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>
```

---

## 🔒 SSL Certificate (HTTPS)

GoDaddy usually provides free SSL:
1. Login to GoDaddy
2. Hosting → Manage
3. Look for "SSL Certificate"
4. Activate free SSL
5. Force HTTPS redirect in `.htaccess`:
```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

---

## 📊 Monitor Performance

### Check These Regularly:
- Google Search Console: Errors, rankings
- Google Analytics: Traffic, users
- PageSpeed Insights: https://pagespeed.web.dev/
- Mobile-friendly test: https://search.google.com/test/mobile-friendly

### Target Scores:
- Performance: > 90
- Accessibility: > 90
- SEO: > 95
- Best Practices: > 90

---

## 🆘 Troubleshooting

### Site Not Loading?
- Clear browser cache
- Check file structure (files in public_html?)
- Verify domain DNS settings

### Images Not Showing?
- Check file paths
- Ensure images uploaded to correct folder
- Check file permissions (644 for images)

### CSS Not Loading?
- Clear cache
- Check if assets folder uploaded
- Verify file paths in index.html

---

## 📞 Need Help?

### Resources:
- GoDaddy Support: 24/7 chat/phone
- Google Search Central: https://developers.google.com/search
- YouTube: Search "GoDaddy hosting tutorial"

---

## ✅ Final Checklist

- [ ] Contact info updated
- [ ] Build completed
- [ ] Files uploaded to GoDaddy
- [ ] Website tested
- [ ] SSL activated
- [ ] Search engines submitted
- [ ] Google My Business created
- [ ] Analytics installed
- [ ] Social media profiles created
- [ ] Local directories listed

---

## 🎉 You're Done!

Your website is now LIVE and SEO-optimized!

**Expected Timeline:**
- Day 1: Site indexed by Google
- Week 1: Start appearing in search
- Month 1: Ranking for long-tail keywords
- Month 3: Significant organic traffic

**Next Steps:**
- Create content regularly
- Build backlinks
- Get client reviews
- Monitor analytics
- Optimize based on data

---

**Good luck with Aadyaa Infotech! 🚀**
