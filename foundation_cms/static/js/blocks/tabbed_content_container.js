export function initTabbedContent() {
  const SELECTORS = {
    tabbedContent: ".tabbed-content-container",
    tabButtons: ".tabbed-content-container__tab-button",
    tabPanels: ".tabbed-content-container__tab-panel",
  };

  const CLASSNAMES = {
    isActive: "is-active",
  };

  const tabbedContents = document.querySelectorAll(SELECTORS.tabbedContent);

  tabbedContents.forEach((container) => {
    const buttons = container.querySelectorAll(SELECTORS.tabButtons);
    const panels = container.querySelectorAll(SELECTORS.tabPanels);

    // Refer content panels by index instead of ID to allow for multiple instances in one page.
    buttons.forEach((button, tabIndex) => {
      button.addEventListener("click", (event) => {
        panels.forEach((panel) => panel.classList.remove(CLASSNAMES.isActive));
        panels[tabIndex].classList.add(CLASSNAMES.isActive);
        buttons.forEach((btn) => btn.classList.remove(CLASSNAMES.isActive));
        button.classList.add(CLASSNAMES.isActive);
        button.scrollIntoView({
          behavior: "smooth",
          block: "nearest",
          inline: "start",
        });
      });
    });
  });

  initTabbedContentCardSets();
}

export function initTabbedContentCardSets() {
  const cardsPerPage = 4;

  const SELECTORS = {
    tabbedContentCardSetPanels:
      ".tabbed-content-container__tab-panel:has(>.tab-card)",
    tabbedContentCard: ".tab-card",
  };

  const CLASSNAMES = {
    tabCardPage: "tab-card__page",
    tabCardPageNav: "tab-card__page-nav",
    tabCardPageNavPrev: "tab-card__page-nav-prev",
    tabCardPageNavCurrent: "tab-card__page-nav-current",
    tabCardPageNavNext: "tab-card__page-nav-next",
  };

  const cardSetPanels = document.querySelectorAll(
    SELECTORS.tabbedContentCardSetPanels,
  );

  cardSetPanels.forEach((panel) => {
    const cards = panel.querySelectorAll(SELECTORS.tabbedContentCard);

    // Wrap cards in pages of 4 cards each
    const pages = Math.ceil(cards.length / cardsPerPage);
    for (let i = 0; i < pages; i++) {
      const page = document.createElement("div");
      page.classList.add(CLASSNAMES.tabCardPage);

      const start = i * cardsPerPage;
      const end = start + cardsPerPage;
      const cardsToShow = Array.from(cards).slice(start, end);

      cardsToShow.forEach((card) => {
        page.appendChild(card);
      });

      panel.appendChild(page);
    }

    if (pages <= 1) {
      return;
    }

    // Create and append navigation controls, previous, page n/n, next
    const nav = document.createElement("div");
    nav.classList.add(CLASSNAMES.tabCardPageNav);

    const prevButton = document.createElement("a");
    prevButton.classList.add(CLASSNAMES.tabCardPageNavPrev);

    const currentPage = document.createElement("span");
    currentPage.classList.add(CLASSNAMES.tabCardPageNavCurrent);
    currentPage.textContent = "1 / " + pages;

    const nextButton = document.createElement("a");
    nextButton.classList.add(CLASSNAMES.tabCardPageNavNext);

    nav.appendChild(prevButton);
    nav.appendChild(currentPage);
    nav.appendChild(nextButton);
    panel.appendChild(nav);

    // Detect initial page index based on scroll position
    let currentPageIndex = 0;
    const initialScrollLeft = panel.scrollLeft;
    const firstPage = panel.querySelector(`.${CLASSNAMES.tabCardPage}`);
    const pageWidth = firstPage ? firstPage.clientWidth : 0;

    if (initialScrollLeft > 0) {
      currentPageIndex = Math.floor(initialScrollLeft / pageWidth);
      currentPage.textContent = `${currentPageIndex + 1} / ${pages}`;
    }

    const nextPage = () => {
      if (currentPageIndex < pages - 1) {
        currentPageIndex++;
        panel.scrollTo({
          left: panel.clientWidth * currentPageIndex,
          behavior: "smooth",
        });
        currentPage.textContent = `${currentPageIndex + 1} / ${pages}`;
      }
    };

    const prevPage = () => {
      if (currentPageIndex > 0) {
        currentPageIndex--;
        panel.scrollTo({
          left: panel.clientWidth * currentPageIndex,
          behavior: "smooth",
        });
        currentPage.textContent = `${currentPageIndex + 1} / ${pages}`;
      }
    };

    nextButton.addEventListener("click", nextPage);
    prevButton.addEventListener("click", prevPage);
  });
}
