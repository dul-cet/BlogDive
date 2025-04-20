import { Routes } from '@angular/router';
import { provideRouter } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { authGuard } from './interceptors/auth.guard';

export const routes: Routes = [
    { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent }, { 
    path: 'dashboard', 
    component: DashboardComponent,
    canActivate: [authGuard] // добавляем защиту маршрута
  },
];

export const appRoutes = provideRouter(routes);