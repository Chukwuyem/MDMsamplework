/*
 Abhimanyu Vasishth & Chukwuyem J Onyibe
 Live project url: https://github.com/Chukwuyem/templestotoilets
*/

console.log("Working on here");

function walk(rootNode){
    // First replace the text of the title
    document.title = replaceText(document.title);

    // Find all the text nodes in rootNode -> which is the document body
    var walker = document.createTreeWalker(
        rootNode,
        NodeFilter.SHOW_TEXT,
        null,
        false
    ),
    node;
    // Modify each text node's value
    while (node = walker.nextNode()) {
    	node.nodeValue = replaceText(node.nodeValue);
    }
}	

function replaceText(text){
    // Temple -> Toilet
    // text = text.replace(/\bTemple(s)?\b/g, "<a href='http://www.cricinfo.com'>Toilet$1</a>");
    text = text.replace(/\bTemple(s)?\b/g, "Toilet$1");
    text = text.replace(/\btemple(s)?\b/g, "toilet$1");
    text = text.replace(/\bTEMPLE(S)?\b/g, "TOILET$1");

    // Home -> Homeless
    text = text.replace(/\bHOME(SCREEN|PAGE)?\b/g, "HOMELESS$1");    
    text = text.replace(/\bHome(screen|page)?\b/g, "Homeless$1");    
    text = text.replace(/\bhome(screen|page)?\b/g, "homeless$1");    

    // Jobs or Careers -> Unemployment
    text = text.replace(/\bJOB(S)?\b/g, "UNEMPLOYMENT");    
    text = text.replace(/\bCAREER(S)?\b/g, "UNEMPLOYMENT");    

    text = text.replace(/\bJob(s)?\b/g, "Unemployment");    
    text = text.replace(/\bCareer(s)?\b/g, "Unemployent");    
    
    text = text.replace(/\bjob(s)?\b/g, "unemployment");    
    text = text.replace(/\bcareer(s)?\b/g, "unemployment");    

    // Privacy -> Exposed
    text = text.replace(/\bPRIVACY\b/g, "EXPOSED");    
    text = text.replace(/\bPrivacy\b/g, "Exposed");    
    text = text.replace(/\bprivacy\b/g, "exposed");        

    // Weather -> Climate Change
    text = text.replace(/\bWEATHER\b/g, "CLIMATE CHANGE");    
    text = text.replace(/\bWeather\b/g, "Climate Change");    
    text = text.replace(/\bweather\b/g, "climate change"); 

    // Ads/Adverts/Advertisements -> Obey
    text = text.replace(/\b(AD(S|s)?|ADVERT(S|s)?|ADVERTISEMENT(S|s)?)\b/g, "OBEY");    
    text = text.replace(/\b(Ad(s)?|Advert(s)?|Advertisement(s)?)\b/g, "Obey");    
    text = text.replace(/\b(ad(s)?|advert(s)?|advertisement(s)?)\b/g, "obey"); 

    text = text.replace(/\bADVERTISING\b/g, "COERCING"); 
    text = text.replace(/\bAdvertising\b/g, "Coercing");
    text = text.replace(/\badvertising\b/g, "coercing");

	return text;
}

var observer = new MutationObserver(function(mutations){
    mutations.forEach(function(mutation){
        // console.log(mutation.type);
        for (var i = 0; i < arrayOfWords.length; i++){
           findWords(arrayOfWords[i], arrayOfLinks[i]);
        }        
        walk(document.body);
    });
});

var config = {
    attributes: true,
    childList: true,
    characterData: true,
    subtree: true
}

// don't replace text within these tags
var arrayOfWords = ["Temple", "Home", "Weather", "Privacy", "Careers"];
var mainUrl = "http://139.59.22.162/";
var arrayOfLinks = [mainUrl, mainUrl + "responses/home", mainUrl + "responses/home", mainUrl + "responses/week1",
                    mainUrl + "responses/week2", mainUrl + "responses/week3", mainUrl + "responses/week4"];

var skipTags = { 'a': 1, 'style': 1, 'script': 1, 'iframe': 1 };

// find text nodes to apply replFn to
function findKW(el,term,replFn){
    var child, tag;

    for (var i = el.childNodes.length - 1; i >= 0; i--) {
        child = el.childNodes[i];


        if (child.nodeType == 1) { // ELEMENT_NODE
            tag = child.nodeName.toLowerCase();
            if (!(tag in skipTags)) {
                findKW(child, term, replFn);
            }
        }
        else if (child.nodeType == 3) { // TEXT_NODE
            replaceKW(child, term, replFn);
        }
    }
}

// replace terms in text according to replFn
function replaceKW( text, term, replFn ) {
    var match,
        matches = [];

    while (match = term.exec(text.data)) {
        matches.push(match);
    }
    for (var i = matches.length - 1; i >= 0; i--) {
        match = matches[i];

        // cut out the text node to replace
        text.splitText(match.index);
        text.nextSibling.splitText(match[1].length);
        text.parentNode.replaceChild(replFn(match[1]), text.nextSibling);
    }
};

function findWords(replTerm, linkTerm){
    findKW(document.body, new RegExp('\\b(' + replTerm + ')\\b', 'g'),
        function (match) {
            var link = document.createElement('a');
            // link.href = 'http://www.cricinfo.com';
            link.href = linkTerm;
            link.innerHTML = match;
            return link;
        }
    );
}

// Got loads of help from here
// Real shoutout to these guys
// http://stackoverflow.com/questions/8949445/javascript-bookmarklet-to-replace-text-with-a-link

// This is based on the millennials to snake people chrome extension
// Look here for more help: https://developer.mozilla.org/en/docs/Web/API/MutationObserver
for (var i = 0; i < arrayOfWords.length; i++){
    findWords(arrayOfWords[i], arrayOfLinks[i]);
}
walk(document.body);
observer.observe(document.body,config);