import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from './navbar/navbar.component'; // Import Navbar
import { FooterComponent } from './footer/footer.component'; // Import Footer

@Component({
  selector: 'app-root',
  template: `
    <app-navbar></app-navbar>
    <div class="container">
      <router-outlet></router-outlet>
    </div>
    <app-footer></app-footer>
  `,
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [RouterOutlet, NavbarComponent, FooterComponent] // Add Components Here
})
export class AppComponent {}
