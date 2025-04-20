// src/main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { appConfig } from './app/app.config';
import { LoginComponent } from './app/components/login/login.component';
import { authGuard } from './app/interceptors/auth.guard';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app/app.component';
bootstrapApplication(AppComponent, {
  providers: [
    provideRouter([
      { path: '', redirectTo: 'login', pathMatch: 'full' },
      {
        path: 'login',
        loadComponent: () => import('./app/components/login/login.component').then(m => m.LoginComponent),
      },
      {
        path: 'dashboard',
        loadComponent: () => import('./app/components/dashboard/dashboard.component').then(m => m.DashboardComponent),
        canActivate: [authGuard]
      }
    ]),
    ...appConfig.providers
  ]
});