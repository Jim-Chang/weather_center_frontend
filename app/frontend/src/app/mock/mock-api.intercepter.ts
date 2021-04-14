import { HTTP_INTERCEPTORS, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

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
export const mockApihttpInterceptorProviders = [
  { provide: HTTP_INTERCEPTORS, useClass: MockApiHttpInterceptor, multi: true },
];
