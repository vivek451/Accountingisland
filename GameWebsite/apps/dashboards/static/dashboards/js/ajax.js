<script>
console.log("I am in ajax call hey how are you")
    debugger;
    function loadAddTransactionForm() {
        $.ajax({
            url: "{% url 'add_transaction' %}", // Replace with the URL of your AddTransactionView
            type: "GET",
            success: function (data) {
                // Load the form into the container
                $('#add-transaction-container').html(data);
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
</script>