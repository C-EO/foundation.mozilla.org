import mobileNavStickinessHandler from "./mobile-nav-stickiness-handler";
import mobileSearchBar from "./mobile-search-bar";
import diveDeeperListExpansionHandler from "./product-page-dive-deeper-list";

/**
 * Bind event handlers
 */
export const bindEventHandlers = () => {
  mobileNavStickinessHandler();
  mobileSearchBar();
  diveDeeperListExpansionHandler();
};
