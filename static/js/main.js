fetch("/config")
    .then((result) => {
        return result.json()
    })
    .then((data) => {
        const stripe = Stripe(data.publicKey)
        document.querySelector("#checkoutbtn").addEventListener("click", () => {
            console.log("click")
            fetch('checkout-session').then(
                (result) => {
                  return result.json()
                }
            ).then(
                (data) => {
                    return stripe.redirectToCheckout({
                        sessionId: data.sessionId})
                }
            )
        })

    })