(function () {
  const cta = document.querySelector(`.callpower-cta`);
  if (!cta) return;

  const { campaignId, newsletter } = cta.dataset;
  console.log(campaignId, newsletter);
  const userPhoneInput = cta.querySelector(`input[name="userPhone"]`);
  const callButton = cta.querySelector(`.make-the-call`);
  callButton.removeAttribute(`disabled`);

  const mainForm = cta.querySelector(`.cta-form`);
  const thankYou = cta.querySelector(`.thank-you`);
  const testbutton = cta.querySelector(`.test-button`);

  console.log(testbutton);

  testbutton.addEventListener(`click`, () => {
    console.log(`swap test`);
    mainForm.classList.add(`tw-hidden`);
    thankYou.classList.remove(`tw-hidden`);
  });

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
})();

