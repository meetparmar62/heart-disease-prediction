# 📧 Email Notification Setup Guide

## Get FREE Email Notifications for Contact Form

### Step 1: Create EmailJS Account (FREE)

1. **Sign Up**
   - Go to: https://dashboard.emailjs.com/signup
   - Create free account
   - No credit card required!

2. **Add Email Service**
   - Click "Add New Service"
   - Select "Gmail" (or your email provider)
   - Connect your Gmail account
   - Copy the **Service ID** (e.g., `service_abc123`)

3. **Create Email Template**
   - Click "Email Templates" → "Create New Template"
   - Click "Load Template" → Choose "Contact Us" template
   
   **Template Content:**
   ```
   Name: {{from_name}}
   Email: {{from_email}}
   Phone: {{phone}}
   Service: {{service}}
   
   Message:
   {{message}}
   
   ---
   Sent from Aadyaa Infotech Website
   ```
   
   - In "Settings" tab:
     - **To Email**: `aadyaainfotech@gmail.com`
     - **From Name**: `{{from_name}}`
     - **Reply-To**: `{{from_email}}`
     - **Subject**: `New Inquiry: {{service}} - {{from_name}}`
   
   - Save and copy the **Template ID** (e.g., `template_xyz789`)

4. **Get Public Key**
   - Go to "Account" (click your name in top right)
   - Under "API Keys" section
   - Copy the **Public Key**

### Step 2: Update Your Code

Open `src/components/Contact.jsx` and replace:

```javascript
// Line ~50: Replace these values
await emailjs.init("YOUR_EMAILJS_PUBLIC_KEY");  // Paste your public key here

await emailjs.send(
    'YOUR_SERVICE_ID',      // Paste your Service ID
    'YOUR_TEMPLATE_ID',      // Paste your Template ID
    {
        // ... rest of the code
    }
);
```

**Example with real values:**
```javascript
await emailjs.init("AbCdEfGhIjKlMnOp");

await emailjs.send(
    'service_abc123',
    'template_xyz789',
    {
        from_name: name,
        from_email: email,
        phone: phone,
        service: service,
        message: message,
        to_email: 'aadyaainfotech@gmail.com',
        reply_to: email
    }
);
```

### Step 3: Test It!

1. Build and deploy your site
2. Fill out the contact form
3. You'll receive an email instantly!
4. Check spam folder if not in inbox

---

## 🎯 Features You Get

✅ **Instant Email Notifications** - Get notified immediately when someone contacts you
✅ **Professional Format** - Clean, organized email layout
✅ **Reply Directly** - Click reply to respond to customer
✅ **Mobile Friendly** - Check emails on phone
✅ **Free Forever** - 200 emails/month free plan
✅ **Backup to WhatsApp** - If email fails, opens WhatsApp automatically

---

## 📊 Visitor Tracking (Already Included!)

Your website now tracks:
- ✅ Total visitors count
- ✅ Page views
- ✅ Visitor details (browser, screen size, location)
- ✅ Referrer source (where they came from)
- ✅ Contact form submissions

### View Analytics in Admin Panel

Press `Ctrl+A` on your website to open admin panel, then check:
- **Inquiries Tracker** - See all contact form submissions
- **Visitor Logs** - Detailed visitor information

---

## 💡 Pro Tips

1. **Upgrade Limits**: Free plan = 200 emails/month. More than enough to start!
2. **Custom Domain**: Use your own email (e.g., `info@aadyaainfotech.in`)
3. **Auto-Reply**: Set up automatic reply to customers
4. **Multiple Recipients**: Add team members to receive emails too

---

## 🆘 Troubleshooting

### Not receiving emails?

1. Check spam/junk folder
2. Verify Service ID and Template ID are correct
3. Make sure Gmail is connected in EmailJS dashboard
4. Check browser console for errors

### Email goes to WhatsApp instead?

This is the backup system! If EmailJS fails, it opens WhatsApp as fallback.

### Want more features?

- SMS notifications: https://www.twilio.com/
- Push notifications: https://webpushr.com/
- Live chat: https://www.tawk.to/

---

## 📱 Alternative: Google Forms (Completely FREE)

If you want simpler solution:

1. Create Google Form: https://forms.google.com/
2. Add your questions
3. Get form embed code
4. Replace contact form in your website

**Pros:**
- Unlimited submissions
- Responses in Google Sheets
- Email notifications included
- No coding needed!

---

**Need Help?** 
EmailJS Support: https://help.emailjs.com/
