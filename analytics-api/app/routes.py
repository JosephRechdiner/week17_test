from fastapi import APIRouter, Request, HTTPException, Depends
from app.dal import Dal

analytics_router = APIRouter()

def get_sql_manager(reauest: Request):
    return reauest.app.state.sql_manager

@analytics_router.get("/analytics/top-customers")
def get_top_customers(sql_manager = Depends(get_sql_manager)):
    cnx = sql_manager.get_cnx()
    customers = Dal.get_top_customer(cnx)
    if not customers:
        raise HTTPException(status_code=404, detail=f"Not found")
    return customers

@analytics_router.get("/analytics/customers-without-orders")
def get_customers_without_orders(sql_manager = Depends(get_sql_manager)):
    cnx = sql_manager.get_cnx()
    customers = Dal.get_customers_without_orders(cnx)
    if not customers:
        raise HTTPException(status_code=404, detail=f"Not found")
    return customers

@analytics_router.get("/analytics/zero-credit-active-customers")
def get_zero_credit_active_customers(sql_manager = Depends(get_sql_manager)):
    cnx = sql_manager.get_cnx()
    customers = Dal.get_zero_credit_active_customers(cnx)
    if not customers:
        raise HTTPException(status_code=404, detail=f"Not found")
    return customers

