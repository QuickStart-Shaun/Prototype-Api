var Webflow = Webflow || [];
Webflow.push(function() {  
  // unbind webflow form handling (keep this if you only want to affect specific forms)
  $(document).off('submit');

  /* Any form on the page */
  $('form').submit(async function(e) {
    e.preventDefault();

    const $form = $(this); // The submitted form
    const $submit = $('[type=submit]', $form); // Submit button of form
    const buttonText = $submit.val(); // Original button text
    const buttonWaitingText = $submit.attr('data-wait'); // Waiting button text value
    const formMethod = $form.attr('method'); // Form method (where it submits to)
    const formAction = $form.attr('action'); // Form action (GET/POST)
    const formRedirect = $form.attr('data-redirect'); // Form redirect location
    const formData = $form.serialize(); // Form data
    const para = document.querySelector('[custom="para"]')
    
    console.log(formData)
    // Set waiting text
    if (buttonWaitingText) {
      $submit.val(buttonWaitingText); 
    }
    
    try {
      const response = await fetch(formAction+"?"+formData, {
        method: formMethod,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });
      console.log(response)
      if (response.ok) {
        const data = await response.json();
        para.innerText = data.result
        console.log(para.innerText)

        // If form redirect setting set, then use this and prevent any other actions
        if (formRedirect) {
          window.location = formRedirect;
          return;
        }

        $form
          .hide() // optional hiding of form
          .siblings('.w-form-done').show() // Show success
          .siblings('.w-form-fail').hide(); // Hide failure
      } else {
        $form
          .siblings('.w-form-done').hide() // Hide success
          .siblings('.w-form-fail').show(); // show failure
      }
    } catch (error) {
      console.error(error);
      $form
        .siblings('.w-form-done').hide() // Hide success
        .siblings('.w-form-fail').show(); // show failure
    } finally {
      // Reset text
      $submit.val(buttonText);
    }
  });
});
