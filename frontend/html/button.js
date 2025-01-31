document.getElementById('orderButton').addEventListener('click', function() {
    // Display order success message
    const orderMessage = document.getElementById('orderMessage');
    orderMessage.textContent = 'Order is successful! Payment method: Credit Card';
    orderMessage.classList.remove('hidden'); // Show the message
  });
  