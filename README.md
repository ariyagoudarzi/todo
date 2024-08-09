
# 🌟 **Todo App** 🌟

Welcome to the **Todo App** 📝! This is a simple yet powerful application built using **HTML**, **CSS**, **JavaScript**, and **Django**. Manage your tasks effortlessly with a sleek interface and intuitive design.

![Todo App Screenshot](https://via.placeholder.com/800x400.png?text=Todo+App+Screenshot)

---

## 🚀 **Features**

- **Easy Task Management**: Add, edit, and delete your tasks with just a few clicks.
- **Responsive Design**: Looks great on all devices, from desktops to smartphones.
- **Dark Mode**: Enjoy a beautiful dark-themed UI that’s easy on the eyes.
- **Smooth Animations**: Experience smooth transitions and interactions throughout the app.

---

## 📂 **File Structure**

Here's a quick overview of the main files in this project:

- **`home.html`**: The main HTML file that serves the Todo app interface.
- **`style.css`**: Contains all the styling and design aspects of the app.
- **`script.js`**: Includes the JavaScript logic for handling user interactions.
- **`Django Backend`**: Powers the backend, handling data persistence and serving dynamic content.

---

## 🎨 **Styling and Design**

The app is designed with a modern and clean look, utilizing the following features:

- **Custom Fonts**: The app uses the **Baloo Bhaijaan 2** font for a friendly and inviting appearance.
- **Dark Theme**: A rich dark color palette to reduce strain on your eyes.
- **Responsive Layout**: Adapts to various screen sizes, ensuring a great experience on any device.
- **Interactive Elements**: Buttons, inputs, and other UI elements are styled for clarity and ease of use.

---

## 🛠️ **How to Run the Project**

To get the Todo App up and running on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/parham006/todo.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd todo
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```
5. **Open the app in your browser**:
   - Go to `http://127.0.0.1:8000` to view the app.

---

## 💻 **Code Snippets**

Here are some key snippets from the project:

### **HTML**
```html
<div class="overlay hidden">
  <div class="plan_box hidden">
    <button class="remove_but">✖️</button>
    <form method="POST" action="/">
      <label class="plan_label">Add your plan</label>
    </form>
  </div>
</div>
```

### **CSS**
```css
body {
  background-color: rgb(28, 28, 28);
  font-family: "Baloo Bhaijaan 2", sans-serif;
}

.addNoteBtn {
  color: #ffffff;
  margin-left: 15px;
  font-size: 18px;
}
```

### **JavaScript**
```javascript
addNoteIcon.addEventListener("click", function () {
  overlay.classList.remove("hidden");
  planBox.classList.remove("hidden");
});

removeBut.addEventListener("click", function () {
  overlay.classList.add("hidden");
  planBox.classList.add("hidden");
});
```

---

## 🤝 **Contributing**

Contributions are welcome! If you have suggestions for improvements or want to report bugs, please open an issue or submit a pull request.

---

## 📄 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 📬 **Contact**

If you have any questions or feedback, feel free to reach out to me at [parham@example.com](mailto:parham@example.com).

---

Enjoy using the Todo App! 🎉
