(function () {
  const cta = document.querySelector(`.callpower-cta`);
  if (!cta) return;

  const { campaignId, newsletter } = cta.dataset;
  const get = cta.querySelector.bind(cta);
  const [userPhoneInput, mainForm, thankYou, callButton] = [
    `input[name="userPhone"]`,
    `.cta-form`,
    `.thank-you`,
    `.make-the-call`,
  ].map(get);
  callButton.removeAttribute(`disabled`);

  const handleCallSubmit = () => {
    const userPhone = userPhoneInput.value;
    const query = `campaignId=${campaignId}&userPhone=${userPhone}`;
    fetch(`https://mozilla.callpower.org/call/create?${query}`, {
      method: "POST",
    })
      .then((response) => {
        if (!response.ok) {
          throw Error(response.statusText);
        }
        return response.json();
      })
      .then((result) => console.log(result))
      .catch((err) => console.error(err));
  };

  callButton.addEventListener(`click`, handleCallSubmit);

  // Testing code
  const toggleButton = cta.querySelector(`.toggle-button`);
  toggleButton.addEventListener(`click`, () => {
    mainForm.classList.toggle(`tw-hidden`);
    thankYou.classList.toggle(`tw-hidden`);
  });
})();
