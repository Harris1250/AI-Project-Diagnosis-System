document.addEventListener('DOMContentLoaded', function () {
    const tags = document.querySelectorAll('.symptom-tag');
    const input = document.querySelector('input[name="symptoms"]');
    const form = document.querySelector('form');
  
    tags.forEach(tag => {
      tag.addEventListener('click', () => {
        const symptom = tag.textContent.trim().toLowerCase();
        input.value = symptom;
        form.submit();
      });
    });
  });
  