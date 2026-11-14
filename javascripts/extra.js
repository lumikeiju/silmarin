/**
 * extra.js
 *
 * @format
 */

/**
 * Title capitalization map
 * Keys use spaces (dashes are handled automatically during matching)
 */
const titleMapSource = {
  josm: "JOSM",
  esr: "ESR",
};

/**
 * Expanded titleMap that includes both space and dash variants.
 * Generated automatically from titleMapSource.
 */
const titleMap = Object.fromEntries(
  Object.entries(titleMapSource).flatMap(([key, value]) => {
    const entries = [[key, value]];
    // If key contains a space, also add the dash variant
    if (key.includes(" ")) {
      entries.push([key.replace(/ /g, "-"), value]);
    }
    return entries;
  })
);

/**
 * Converts a string to Title Case.
 * @param {string} str - The string to convert
 * @returns {string} - The string in Title Case
 */
function toTitleCase(str) {
  return str.replace(/\w\S*/g, (word) => {
    return word.charAt(0).toUpperCase() + word.substr(1).toLowerCase();
  });
}

/**
 * Applies correct capitalization to a text string based on titleMap.
 * Falls back to Title Case for unmatched text.
 * @param {string} text - The text to transform
 * @returns {string} - The text with correct capitalization
 */
function applyTitleCapitalization(text) {
  if (!text) return text;

  const trimmedText = text.trim();
  const lowerText = trimmedText.toLowerCase();

  // Check for exact match first (handles both space and dash variants)
  if (titleMap[lowerText]) {
    return titleMap[lowerText];
  }

  // Apply mapped terms first, then Title Case the rest
  let result = trimmedText;

  // Track which parts have been replaced by titleMap entries
  const replacements = [];

  for (const [key, value] of Object.entries(titleMapSource)) {
    // Create regex to match the key with spaces or dashes interchangeably
    const pattern = key.replace(/ /g, "[- ]");
    const regex = new RegExp(`\\b${pattern}\\b`, "gi");
    result = result.replace(regex, (match) => {
      replacements.push({ original: match, replacement: value });
      // Use a placeholder to protect this from Title Case transformation
      return `\x00${replacements.length - 1}\x00`;
    });
  }

  // Apply Title Case to any remaining text (not matched by titleMap)
  result = toTitleCase(result);

  // Restore the titleMap replacements
  replacements.forEach((r, i) => {
    result = result.replace(`\x00${i}\x00`, r.replacement);
  });

  return result;
}

/**
 * Applies title capitalization to a single element's text content.
 * @param {Element} element - The DOM element to fix
 */
function fixElementCapitalization(element) {
  if (!element) return;

  // Handle elements with mixed content (text + icons)
  const childNodes = Array.from(element.childNodes);
  childNodes.forEach((node) => {
    if (node.nodeType === Node.TEXT_NODE && node.textContent.trim()) {
      const original = node.textContent;
      const fixed = applyTitleCapitalization(original);
      if (original !== fixed) {
        node.textContent = fixed;
      }
    }
  });
}

/**
 * Applies title capitalization to all navigation elements.
 * Targets: navigation tabs, sidebar nav items, TOC entries, breadcrumbs.
 */
function fixNavigationCapitalization() {
  // All navigation link selectors
  const selectors = [
    ".md-tabs__link", // Top navigation tabs
    ".md-nav__link", // All nav links (sidebar + TOC)
    ".md-path__link", // Breadcrumb links
    ".md-header__topic", // Header topic text
    ".md-ellipsis", // Truncated nav items
  ];

  const allElements = document.querySelectorAll(selectors.join(", "));
  allElements.forEach(fixElementCapitalization);
}

/**
 * Initialize with aggressive monitoring for instant navigation.
 */
(function initCapitalizationFixes() {
  // Apply fixes immediately and repeatedly during initial load
  fixNavigationCapitalization();

  // Apply again after short delays to catch async renders
  setTimeout(fixNavigationCapitalization, 100);
  setTimeout(fixNavigationCapitalization, 250);
  setTimeout(fixNavigationCapitalization, 500);

  // Create a global observer on document body to catch ALL changes
  const observer = new MutationObserver(() => {
    // Use requestAnimationFrame for smoother updates
    requestAnimationFrame(fixNavigationCapitalization);
  });

  // Start observing once body is available
  const startObserving = () => {
    observer.observe(document.body, {
      childList: true,
      subtree: true,
      characterData: true,
      characterDataOldValue: false,
    });
  };

  if (document.body) {
    startObserving();
  } else {
    document.addEventListener("DOMContentLoaded", startObserving);
  }

  // Hook into all possible navigation events
  document.addEventListener("DOMContentLoaded", fixNavigationCapitalization);
  window.addEventListener("load", fixNavigationCapitalization);
  window.addEventListener("hashchange", fixNavigationCapitalization);
  window.addEventListener("popstate", fixNavigationCapitalization);

  // The instant loading feature dispatches a custom event
  document.addEventListener("DOMContentSwitch", fixNavigationCapitalization);

  // Also use location subscription if available
  if (typeof location$ !== "undefined") {
    location$.subscribe(() => {
      setTimeout(fixNavigationCapitalization, 0);
      setTimeout(fixNavigationCapitalization, 100);
    });
  }

  // Fallback: periodic check for first few seconds after load
  let checkCount = 0;
  const periodicCheck = setInterval(() => {
    fixNavigationCapitalization();
    checkCount++;
    if (checkCount >= 20) {
      // Stop after ~10 seconds
      clearInterval(periodicCheck);
    }
  }, 500);
})();
