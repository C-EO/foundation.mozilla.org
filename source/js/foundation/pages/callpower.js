(function () {
    const elements = document.querySelectorAll(`.streamfield-content .callpower`);

    for (element of elements) {
      const campaignIdInput = element.querySelector(`input[name="campaignId"]`);
      const userPhoneInput = element.querySelector(`input[name="userPhone"]`);
      const callButton = element.querySelector(`.make-the-call`);

      callButton.addEventListener(`click`, () => {
        const campaignId = campaignIdInput.value;
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
      });
    }
  })();
