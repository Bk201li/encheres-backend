def auction_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        from api.models import Auction
        from datetime import datetime, timedelta

        auctions = Auction.objects.filter(end=False)
        for auction in auctions:
            if datetime.now() - auction.updated_at > (datetime.now() - auction.updated_at) + timedelta(minutes=60):
                auction.end = True
                auction.save()

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware