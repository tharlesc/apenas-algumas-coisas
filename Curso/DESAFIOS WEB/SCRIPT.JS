// Sample product data
const products = [
    { id: 1, name: "Product 1", price: 10.0 },
    { id: 2, name: "Product 2", price: 15.0 },
    { id: 3, name: "Product 3", price: 20.0 },
  ];
  
  const productList = document.querySelector(".product-list");
  const cartItems = document.querySelector(".cart-items");
  const totalElement = document.getElementById("total");
  
  let cart = [];
  
  // Render products
  function renderProducts() {
    products.forEach((product) => {
      const productDiv = document.createElement("div");
      productDiv.classList.add("product");
      productDiv.innerHTML = `
        <h3>${product.name}</h3>
        <p>Price: $${product.price.toFixed(2)}</p>
        <button onclick="addToCart(${product.id})">Add to Cart</button>
      `;
      productList.appendChild(productDiv);
    });
  }
  
  // Add product to cart
  function addToCart(productId) {
    const product = products.find((p) => p.id === productId);
    cart.push(product);
    renderCart();
  }
  
  // Render cart
  function renderCart() {
    cartItems.innerHTML = "";
    let total = 0;
  
    cart.forEach((item, index) => {
      const cartItem = document.createElement("li");
      cartItem.textContent = `${item.name} - $${item.price.toFixed(2)}`;
      const removeButton = document.createElement("button");
      removeButton.textContent = "Remove";
      removeButton.onclick = () => removeFromCart(index);
      cartItem.appendChild(removeButton);
      cartItems.appendChild(cartItem);
  
      total += item.price;
    });
  
    totalElement.textContent = total.toFixed(2);
  }
  
  // Remove item from cart
  function removeFromCart(index) {
    cart.splice(index, 1);
    renderCart();
  }
  
  // Initialize
  renderProducts();