const fs = require('fs');
const js = fs.readFileSync('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'utf8');

// Just syntax check the JS
try {
  new Function(js);
  console.log("Syntax is valid");
} catch (e) {
  console.log("Syntax Error:", e);
}
