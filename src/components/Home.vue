<template>
  <div>
    <!-- Navigation -->
    <nav class="navbar navbar-dark absolute-top">
      <div class="container">
        <a class="navbar-brand" href="#">Garden Hub</a>
      </div>
    </nav>

    <!-- Masthead -->
    <header class="masthead text-white text-center">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-xl-9 mx-auto">
            <h1 class="mb-5">Join a Community Garden!</h1>
            <button
              class="btn btn-lg btn-join"
              @click="() => this.$router.push('find-gardens')"
            >JOIN NOW</button>
          </div>
        </div>
      </div>
    </header>

    <!-- Icons Grid -->
    <section class="features-icons bg-light text-center">
      <div class="container">
        <div class="row">
          <div class="col-lg-4">
            <div class="features-icons-item mx-auto mb-5 mb-lg-0 mb-lg-3">
              <div class="features-icons-icon d-flex">
                <i class="icon-bulb m-auto text-success"></i>
              </div>
              <h3>Grow</h3>
              <p
                class="lead mb-0"
              >Grow healthy vegetables and fruits locally to increase food resiliency and accessibility.</p>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="features-icons-item mx-auto mb-5 mb-lg-0 mb-lg-3">
              <div class="features-icons-icon d-flex">
                <i class="icon-emotsmile m-auto text-success"></i>
              </div>
              <h3>Learn</h3>
              <p
                class="lead mb-0"
              >Learn about why local food matters, how to take care of your crops, and share your food production knowledge with the community.</p>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="features-icons-item mx-auto mb-0 mb-lg-3">
              <div class="features-icons-icon d-flex">
                <i class="icon-heart m-auto text-success"></i>
              </div>
              <h3>Connect</h3>
              <p
                class="lead mb-0"
              >Enagage with your fellow residents and interact with the community.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Image Showcases -->
    <section class="showcase">
      <div class="container">
        <div class="row no-gutters">
          <div class="col-lg-6 order-lg-2 text-white showcase-img showcase-vision"></div>
          <div class="col-lg-6 order-lg-1 my-auto showcase-text">
            <h2>Our Vision</h2>
            <p
              class="lead mb-0"
            >Climate change will affect global food markets in unprecedented ways.</p>
            <br>
            <p class="lead mb-0">
              A global awareness of these challenges must be addressed with
              local action to prepare Vancouver’s food systems for a more self-sustained future.
            </p>
          </div>
        </div>
        <!-- <div class="row no-gutters">
          <div
            class="col-lg-6 text-white showcase-img"
            style="background-image: url('img/bg-showcase-2.jpg');"
          ></div>
          <div class="col-lg-6 my-auto showcase-text">
            <h2>Updated For Bootstrap 4</h2>
            <p
              class="lead mb-0"
            >Newly improved, and full of great utility classes, Bootstrap 4 is leading the way in mobile responsive web development! All of the themes on Start Bootstrap are now using Bootstrap 4!</p>
          </div>
        </div>
        <div class="row no-gutters">
          <div
            class="col-lg-6 order-lg-2 text-white showcase-img"
            style="background-image: url('img/bg-showcase-3.jpg');"
          ></div>
          <div class="col-lg-6 order-lg-1 my-auto showcase-text">
            <h2>Easy to Use &amp; Customize</h2>
            <p
              class="lead mb-0"
            >Landing Page is just HTML and CSS with a splash of SCSS for users who demand some deeper customization options. Out of the box, just add your content and images, and your new landing page will be ready to go!</p>
          </div>
        </div>-->
      </div>
    </section>

    <!-- Testimonials -->
    <!-- <section class="testimonials text-center bg-light">
      <div class="container">
        <h2 class="mb-5">What people are saying...</h2>
        <div class="row">
          <div class="col-lg-4">
            <div class="testimonial-item mx-auto mb-5 mb-lg-0">
              <img class="img-fluid rounded-circle mb-3" src="img/testimonials-1.jpg" alt>
              <h5>Margaret E.</h5>
              <p class="font-weight-light mb-0">"This is fantastic! Thanks so much guys!"</p>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="testimonial-item mx-auto mb-5 mb-lg-0">
              <img class="img-fluid rounded-circle mb-3" src="img/testimonials-2.jpg" alt>
              <h5>Fred S.</h5>
              <p
                class="font-weight-light mb-0"
              >"Bootstrap is amazing. I've been using it to create lots of super nice landing pages."</p>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="testimonial-item mx-auto mb-5 mb-lg-0">
              <img class="img-fluid rounded-circle mb-3" src="img/testimonials-3.jpg" alt>
              <h5>Sarah W.</h5>
              <p
                class="font-weight-light mb-0"
              >"Thanks so much for making these free resources available to us!"</p>
            </div>
          </div>
        </div>
      </div>
    </section>-->

    <!-- Call to Action -->
    <!-- <section class="call-to-action text-white text-center">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-xl-9 mx-auto">
            <h2 class="mb-4">Ready to get started? Sign up now!</h2>
          </div>
          <div class="col-md-10 col-lg-8 col-xl-7 mx-auto">
            <form>
              <div class="form-row">
                <div class="col-12 col-md-9 mb-2 mb-md-0">
                  <input
                    type="email"
                    class="form-control form-control-lg"
                    placeholder="Enter your email..."
                  >
                </div>
                <div class="col-12 col-md-3">
                  <button type="submit" class="btn btn-block btn-lg btn-primary">Sign up!</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>-->

    <!-- Footer -->
    <footer class="footer bg-light">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 h-100 text-center text-lg-left my-auto">
            <ul class="list-inline mb-2">
              <li class="list-inline-item">
                <a href="#">Contact</a>
              </li>
              <li class="list-inline-item">&sdot;</li>
              <li class="list-inline-item">
                <a href="#">Terms of Use</a>
              </li>
              <li class="list-inline-item">&sdot;</li>
              <li class="list-inline-item">
                <a href="#">Privacy Policy</a>
              </li>
            </ul>
            <p class="text-muted small mb-4 mb-lg-0">&copy; Garden Hub 2019. All Rights Reserved.</p>
          </div>
          <div class="col-lg-6 h-100 text-center text-lg-right my-auto">
            <ul class="list-inline mb-0">
              <li class="list-inline-item mr-3">
                <a href="#">
                  <i class="fab fa-facebook fa-2x fa-fw"></i>
                </a>
              </li>
              <li class="list-inline-item mr-3">
                <a href="#">
                  <i class="fab fa-twitter-square fa-2x fa-fw"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                  <i class="fab fa-instagram fa-2x fa-fw"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
a {
  color: #28a745;
}

.absolute-top {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1030;
}

.showcase-vision {
  background-image: url("../img/bg-garden-showcase.jpg");
  padding: 16px;
  border-radius: 64px;
  background-clip: content-box;
}

.btn-join {
  color: white;
  background-color: rgb(241, 139, 4);
  border-color: rgb(241, 139, 4);
  border-radius: 32px;
  padding: 16px 32px;
  letter-spacing: 2px;
  font-weight: 700;
  outline: none;
}

.btn-join:hover,
.btn-join:focus {
  color: white;
  background-color: rgb(248, 161, 46);
  border-color: rgb(248, 161, 46);
  outline: none;
}
</style>