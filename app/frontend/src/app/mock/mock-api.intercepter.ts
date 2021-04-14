import { HTTP_INTERCEPTORS, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Injectable, Provider } from '@angular/core';
import { Observable } from 'rxjs';

import { environment as env } from 'src/environments/environment';
import { weatherApiHandler } from './mock-weather-api.config';

@Injectable()
class MockApiHttpInterceptor implements HttpInterceptor {
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const mockEndpointHandler = weatherApiHandler(request);
    if (mockEndpointHandler) {
      console.log('[MockApiHttpInterceptor]', request.url, request.params);
      return mockEndpointHandler(request);
    }
    return next.handle(request);
  }
}

/**
 * How to use:
 * Add this `mockApihttpInterceptorProviders` to providers in AppModule
 */
export function getMockApihttpInterceptorProviders(): Provider[] {
  let mockApihttpInterceptorProviders: any[] = [];
  if (env.isMockApi) {
    mockApihttpInterceptorProviders = [
      { provide: HTTP_INTERCEPTORS, useClass: MockApiHttpInterceptor, multi: true },
    ];
  }
  return mockApihttpInterceptorProviders;
}

