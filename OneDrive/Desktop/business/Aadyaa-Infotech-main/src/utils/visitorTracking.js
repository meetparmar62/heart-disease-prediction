// Visitor Tracking System
const VISITOR_API_URL = 'https://api.countapi.xyz/hit';
const SITE_ID = 'aadyaainfotech.in';

export const trackVisitor = async () => {
  try {
    // Track page visit
    const response = await fetch(`${VISITOR_API_URL}/${SITE_ID}`);
    const data = await response.json();
    
    // Get visitor details
    const visitorInfo = {
      visits: data.value,
      timestamp: new Date().toISOString(),
      userAgent: navigator.userAgent,
      referrer: document.referrer,
      page: window.location.href,
      screen: `${window.screen.width}x${window.screen.height}`,
      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
    };
    
    // Store in localStorage for admin panel
    const allVisits = JSON.parse(localStorage.getItem('visitorLogs') || '[]');
    allVisits.push(visitorInfo);
    localStorage.setItem('visitorLogs', JSON.stringify(allVisits));
    
    console.log('Visitor tracked:', visitorInfo);
    return visitorInfo;
  } catch (error) {
    console.error('Error tracking visitor:', error);
    return null;
  }
};

export const getVisitorCount = async () => {
  try {
    const response = await fetch(`${VISITOR_API_URL}/${SITE_ID}`);
    const data = await response.json();
    return data.value;
  } catch (error) {
    console.error('Error getting visitor count:', error);
    return 0;
  }
};

export const trackPageView = async (pageName) => {
  try {
    await fetch(`${VISITOR_API_URL}/${SITE_ID}/${pageName}`);
  } catch (error) {
    console.error('Error tracking page view:', error);
  }
};
