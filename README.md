# Improving Web Logging using X-Forwarded-For

This project enhances traditional web server logging by incorporating the `X-Forwarded-For` (XFF) HTTP header to more accurately capture the original client IP address—especially useful in environments with proxies, load balancers, or CDN services. By parsing and validating the XFF header, this solution ensures more reliable IP tracking for auditing, analytics, and security monitoring.

## Features

- Extracts original client IPs from `X-Forwarded-For` headers  
- Supports configurable trusted proxy chains  
- Works with popular web servers (e.g., Nginx, Apache) and frameworks  
- Enhances existing logging formats with accurate IP information  
- Mitigates spoofing with optional IP validation  

## Use Cases

- Real client IP logging behind reverse proxies  
- Accurate geolocation and rate-limiting  
- Improved security incident tracing  
